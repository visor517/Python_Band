# Generated by Django 3.2.12 on 2022-04-16 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0002_auto_20220406_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='article_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
