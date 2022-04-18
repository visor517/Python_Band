from uuid import uuid4

from django.db import models
from django.urls import reverse
from authapp.models import HabrUser
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


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
    content = RichTextField(blank=True, null=True)
    #content = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(HabrUser, on_delete=models.DO_NOTHING,
                               verbose_name="Автор")
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 verbose_name="Категория")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    image = models.ImageField(upload_to='article_photos/', blank=True, null=True, verbose_name='Изображение')
    status = models.CharField(choices=STATUSES, max_length=128, default='DF')
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.uid])

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
