# Generated by Django 3.2.12 on 2022-04-12 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articleapp', '0002_auto_20220406_1708'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
                ('comment_create', models.DateTimeField(auto_now_add=True)),
                ('comment_update', models.DateTimeField(auto_now=True)),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleapp.article', verbose_name='Статья')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'db_table': 'comments',
            },
        ),
    ]
