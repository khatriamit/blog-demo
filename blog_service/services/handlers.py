from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import Blog
from blog_service.services.serializer import BlogSerializer
from blog_service.domain import commands
from blog_service.adapter import views


class BlogView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = commands.BlogPost(blog=serializer.validated_data)
        views.create_blog_post(cmd=cmd, created_by=self.request.user)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
