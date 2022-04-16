# Generated by Django 3.2.12 on 2022-04-14 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0002_auto_20220406_1708'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commentapp', '0005_alter_comments_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_articles', to='articleapp.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
    ]