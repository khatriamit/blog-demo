from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth_service.services.handlers import (
    UserViewSet,
    RegisterUserViewSet,
    ChangePasswordViewSet,
)

router = DefaultRouter()
router.register("users", UserViewSet, basename="post")
router.register("register", RegisterUserViewSet, basename="register")


urlpatterns = [
    path("", include(router.urls)),
    path("change_password/", ChangePasswordViewSet.as_view()),
]
