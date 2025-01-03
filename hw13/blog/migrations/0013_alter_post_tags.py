# Generated by Django 4.1 on 2024-12-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="blog.tag"
            ),
        ),
    ]
