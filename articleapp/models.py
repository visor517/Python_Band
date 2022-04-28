from uuid import uuid4

from django.db import models
from django.urls import reverse
from authapp.models import HabrUser
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
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
    content = RichTextField(verbose_name='Текст', blank=True, null=True)
    author = models.ForeignKey(HabrUser, on_delete=models.DO_NOTHING,
                               verbose_name="Автор")
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 verbose_name="Категория")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    image = models.ImageField(upload_to='article_photos/', blank=True, null=True, verbose_name='Изображение')
    status = models.CharField(choices=STATUSES, max_length=128, default='DF')
    liked = models.ManyToManyField(HabrUser, blank=True, related_name='likes')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.uid])

    def delete(self, using=None, keep_parents=False):
        self.status = 'DT'
        self.save()

    @property
    def num_likes(self):
        """
        :return:
        """
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Dislike', 'Dislike')
)


class Like(models.Model):
    """
    класс - Лайки
    """
    user = models.ForeignKey(HabrUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',
                             max_length=8)

    def __str__(self):
        """
        :return:
        """
        return str(self.article)
