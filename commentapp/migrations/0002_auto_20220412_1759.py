# Generated by Django 3.2.12 on 2022-04-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_moderation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
