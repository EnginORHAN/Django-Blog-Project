# Generated by Django 4.2.8 on 2023-12-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50, verbose_name='Başlık Deneme')),
            ],
        ),
    ]
