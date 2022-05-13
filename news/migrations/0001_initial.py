# Generated by Django 3.2.12 on 2022-05-07 01:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст новости')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновленна')),
                ('status', models.CharField(choices=[('DF', 'Черновик'), ('PB', 'Опубликованно'), ('DT', 'Удалённо')], default='DF', max_length=128, verbose_name='Статус новости')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/news_photos/', verbose_name='Новостное изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
