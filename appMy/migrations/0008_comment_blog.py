# Generated by Django 4.2.8 on 2023-12-30 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_comment_fullname_alter_comment_date_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.blog', verbose_name='blog'),
        ),
    ]