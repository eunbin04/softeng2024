# Generated by Django 4.1 on 2024-12-23 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("single_pages", "0012_rename_bio_teammember_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Raspberry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("app", "App"),
                            ("product", "Product"),
                            ("branding", "Branding"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="raspberry/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "project_url",
                    models.URLField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="프로젝트 URL",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Warning",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("hook_text", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="warning/")),
            ],
        ),
        migrations.RemoveField(
            model_name="portfolio",
            name="author",
        ),
        migrations.DeleteModel(
            name="TeamMember",
        ),
        migrations.DeleteModel(
            name="Portfolio",
        ),
    ]
