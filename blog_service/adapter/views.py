from blog_service.domain import models
from blog_service.domain import commands
from blog_service.adapter import repository


def create_blog_post(cmd: commands.BlogPost, created_by):
    models.blog_post_factory(
        title=cmd.blog.get("title"),
        heading=cmd.blog.get("heading"),
        body=cmd.blog.get("body"),
        created_by=created_by,
    )
    repository_ = repository.BlogPostSQLRepository()
    repository_.create(
        title=cmd.blog.get("title"),
        heading=cmd.blog.get("heading"),
        body=cmd.blog.get("body"),
        created_by=created_by,
    )
