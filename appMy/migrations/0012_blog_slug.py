# Generated by Django 4.2.8 on 2024-01-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0011_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
    ]
