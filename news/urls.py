from django.urls import path
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.news_main, name='main'),
    path('create_news', views.create_news, name='create_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete')
]