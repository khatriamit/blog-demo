from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_service.services.handlers import BlogView

router = DefaultRouter()
router.register("post", BlogView, basename="post")

urlpatterns = [
    path("", include(router.urls)),
]
