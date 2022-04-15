from django.db import models
from authapp.models import HabrUser
from articleapp.models import Article


class Comments(models.Model):
    """
    класс - Комментарии
    """
    class Meta:
        """
        класс - Мета
        """
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    comment_author = models.ForeignKey(HabrUser,
                                       verbose_name='Автор комментария',
                                       on_delete=models.CASCADE)
    comment_article = models.ForeignKey(Article,
                                        verbose_name='Статья',
                                        on_delete=models.CASCADE,
                                        related_name='comments_articles')
    comment_text = models.TextField('Комментарий')
    comment_create = models.DateTimeField('Дата создания', auto_now_add=True)
    comment_update = models.DateTimeField('Дата обновления', auto_now=True)
    comment_moderation = models.BooleanField('Модерация', default=False)

    def __str__(self):
        """
        :return:
        """
        return "{}".format(self.comment_author)
