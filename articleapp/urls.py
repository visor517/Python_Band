from django.urls import path

from articleapp.views import IndexView, ArticleDetailView, \
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView, AddLike, Dislike, ArticleListView
from mainapp.views import main



app_name = 'articleapp'

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('index/', IndexView.as_view(), name='main'),
    path('article/new/', ArticleCreateView.as_view(), name='add'),
    path('article/list/', ArticleListView.as_view(), name='list'),
    path('article/<uuid:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('article/<uuid:pk>/like/', AddLike.as_view(), name='like'),
    path('article/<uuid:pk>/dislike/', Dislike.as_view(), name='dislike'),
    path('article/<uuid:pk>/edit/', ArticleUpdateView.as_view(), name='edit'),
    path('article/<uuid:pk>/delete/', ArticleDeleteView.as_view(),
         name='delete'),
]
