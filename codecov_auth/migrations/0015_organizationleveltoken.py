# Generated by Django 3.2.12 on 2022-08-17 18:35

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("codecov_auth", "0014_alter_repositorytoken_token_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganizationLevelToken",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("external_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("token", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("valid_until", models.DateTimeField(blank=True, null=True)),
                (
                    "token_type",
                    models.CharField(choices=[("upload", "Upload")], max_length=50),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        db_column="ownerid",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_tokens",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
