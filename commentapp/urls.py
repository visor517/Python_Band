from django.urls import path
from .views import update_comment_moderation

app_name = 'commentapp'

urlpatterns = [
    path('update_comment_moderation/<int:pk>/<slug:type>',
         update_comment_moderation, name='update_comment_moderation'),
]
