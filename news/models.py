from django.db import models
from authapp.models import HabrUser


class News(models.Model):
    author = models.ForeignKey(HabrUser, on_delete=models.DO_NOTHING,
                               verbose_name="Автор")
    title = models.CharField(verbose_name="Название", max_length=50)
    anons = models.CharField(verbose_name="Анонс", max_length=250)
    full_text = models.TextField(verbose_name='Статья')
    date = models.DateTimeField(verbose_name="Дата публикации", auto_now=True)
    image = models.ImageField(upload_to='media/news_photos/', blank=True, null=True, verbose_name='Новостное изображение')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
