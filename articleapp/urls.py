from django.urls import path

from articleapp.views import ArticleListView, ArticleDetailView, \
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from mainapp.views import main
from commentapp.views import update_comment_moderation

app_name = 'articleapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='main'),
    path('index/', ArticleListView.as_view(), name='main'),
    path('article/new/', ArticleCreateView.as_view(), name='add'),
    path('article/<uuid:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('article/<uuid:pk>/edit/', ArticleUpdateView.as_view(), name='edit'),
    path('article/<uuid:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('update_comment_moderation/<int:pk>/<slug:type>',
             update_comment_moderation, name='update_comment_moderation'),
]
