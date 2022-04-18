from django.urls import path

from articleapp.views import ArticleListView, ArticleDetailView, \
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from mainapp.views import main
from .views import AddLike, Dislike

app_name = 'articleapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='main'),
    path('index/', ArticleListView.as_view(), name='main'),
    path('article/new/', ArticleCreateView.as_view(), name='add'),
    path('article/<uuid:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('article/<uuid:pk>/like', AddLike.as_view(), name='like'),
    path('article/<uuid:pk>/dislike', Dislike.as_view(), name='dislike'),
    path('article/<uuid:pk>/edit/', ArticleUpdateView.as_view(), name='edit'),
    path('article/<uuid:pk>/delete/', ArticleDeleteView.as_view(),
         name='delete'),
]
