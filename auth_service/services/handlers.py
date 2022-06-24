from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from app.models import User
from auth_service.services.serializer import (
    UserSerializer,
    RegisterUserSerializer,
    ChangePasswordSerializer,
)
from auth_service.domain import commands
from auth_service.adapter import views


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    allowed_heads = ["get"]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class RegisterUserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    allowed_heads = ["post"]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.RegisterUser(**serializer.validated_data)
        views.register_user(cmd=cmd)

        return Response(
            {"success": "user registered successfully"},
            status=status.HTTP_201_CREATED,
        )


class ChangePasswordViewSet(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"success": "password changed successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
