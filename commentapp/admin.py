from django.contrib import admin
from commentapp.models import Comments


class CommentAdmin(admin.ModelAdmin):
    """
    класс - Комментарии в админке
    """
    list_display = (
        'comment_author',
        'comment_article',
        'comment_text',
        'comment_create',
        'comment_update',
        'comment_moderation'
    )


admin.site.register(Comments, CommentAdmin)
