# Generated by Django 3.0.4 on 2020-08-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0003_auto_20200829_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='uslusgi',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
