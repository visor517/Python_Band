# Generated by Django 3.2.12 on 2022-04-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0002_auto_20220418_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='likes',
        ),
    ]