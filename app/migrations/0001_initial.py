# Generated by Django 4.0.4 on 2022-05-25 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('title', models.CharField(max_length=150)),
                ('heading', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'db_table': 'blog',
                'ordering': ['created_on'],
            },
        ),
    ]
