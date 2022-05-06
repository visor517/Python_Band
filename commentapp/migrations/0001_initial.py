# Generated by Django 3.2.12 on 2022-05-01 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
                ('comment_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('comment_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('comment_moderation', models.BooleanField(default=True, verbose_name='Модерация')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_articles', to='articleapp.article', verbose_name='Статья')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'comments',
            },
        ),
    ]
