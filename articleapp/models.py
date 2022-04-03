from uuid import uuid4

from django.db import models

# Create your models here.
from django.urls import reverse

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)


class Article(models.Model):
    DRAFT = 'DF'
    PUBLISHED = 'PB'
    DELETED = 'DT'
    STATUSES = (
        (DRAFT, 'черновик'),
        (PUBLISHED, 'опубликованный'),
        (DELETED, 'удалённый'),
    )
    uid = models.UUIDField(verbose_name='Ид', primary_key=True, default=uuid4)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               verbose_name="Автор")
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 verbose_name="Категория", )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    image = models.ImageField(upload_to='media/article_photos/', blank=True, null=True, verbose_name='Изображение')
    status = models.CharField(choices=STATUSES, max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.uid])
