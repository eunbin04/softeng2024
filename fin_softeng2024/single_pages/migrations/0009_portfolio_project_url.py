# Generated by Django 4.1 on 2024-12-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("single_pages", "0008_portfolio_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="project_url",
            field=models.URLField(
                blank=True, max_length=300, null=True, verbose_name="프로젝트 URL"
            ),
        ),
    ]