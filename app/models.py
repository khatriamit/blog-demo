from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CommonInfo(models.Model):
    """
    common info that is frequently to be used in every model
    """

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, db_index=True
    )
    created_on = models.DateTimeField("Created at", auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(
        User,
        verbose_name="Created by",
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
    )
    modified_on = models.DateTimeField("Last modified at", auto_now=True, db_index=True)
    modified_by = models.ForeignKey(
        User,
        verbose_name="Modified by",
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True


class Blog(CommonInfo):
    title = models.CharField(max_length=150)
    heading = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["created_on"]
        db_table = "blog"
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
