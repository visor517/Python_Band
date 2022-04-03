from django.urls import path

from mainapp.views import ArticleListView, ArticleDetailView, \
    ArticleCreateView,  ArticleUpdateView, ArticleDeleteView
from mainapp.views import main

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('index/', main),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<uuid:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<uuid:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<uuid:pk>/delete/', ArticleDeleteView.as_view(), name ='article_delete'),

]
