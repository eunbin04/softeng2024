# Generated by Django 4.1 on 2024-12-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("single_pages", "0003_portfolio_category_alter_portfolio_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="image",
            field=models.ImageField(upload_to="testimonials/"),
        ),
    ]