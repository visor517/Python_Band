from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50)
    anons = models.CharField(verbose_name="Анонс", max_length=250)
    full_text = models.TextField(verbose_name='Статья')
    date = models.DateTimeField(verbose_name="Дата публикации", auto_now=True)

    def __str__(self) -> str:
        return self.title
