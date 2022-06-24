import typing
from app import models as orm
from django.db import transaction
from blog_service.domain import models


class BlogPostSQLRepository:
    def __init__(self) -> None:
        pass

    def create(self, title, heading, body, created_by):
        with transaction.atomic():
            blog = orm.Blog.objects.create(
                title=title,
                heading=heading,
                body=body,
                created_by=created_by,
            )
            return blog
