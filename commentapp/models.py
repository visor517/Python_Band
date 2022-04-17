from django.db import models
from authapp.models import HabrUser
from articleapp.models import Article
from .middleware import get_current_user


class FilterComments(models.Manager):
    """
    класс - Фильтр комментариев
    """

    def get_queryset(self):
        """
        :return:
        """
        user = get_current_user()
        if not user.is_authenticated:
            return super().get_queryset().filter(comment_moderation=True)
        return super().get_queryset().filter(
            models.Q(comment_moderation=False,
                     comment_author=get_current_user()) |
            models.Q(comment_moderation=False,
                     comment_article__author=get_current_user()) |
            models.Q(comment_moderation=True))


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
    objects = FilterComments()

    def __str__(self):
        """
        :return:
        """
        return "{}".format(self.comment_author)
