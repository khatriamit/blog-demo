from django.db import transaction
from rest_framework import serializers
from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8, write_only=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    username = serializers.CharField(max_length=50, required=True)
    confirm_password = serializers.CharField(
        max_length=50, min_length=8, write_only=True
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "confirm_password",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "password did not match"})

        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError({"username": "username already exists"})

        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({"email": "email already exists"})
        return super().validate(attrs)

    @transaction.atomic
    def create(self, validate_data):
        validate_data.pop("confirm_password")
        user = User.objects.create_user(**validate_data)
        user.set_password(validate_data.get("password"))
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=50, required=True)
    confirm_password = serializers.CharField(max_length=50, required=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "password did not match"})
        return super().validate(attrs)

    model = User
