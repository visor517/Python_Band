# Generated by Django 3.2.12 on 2022-05-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_photos/', verbose_name='Изображение'),
        ),
    ]
