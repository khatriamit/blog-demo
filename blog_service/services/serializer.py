from rest_framework import serializers
from app.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "heading",
            "body",
        ]
