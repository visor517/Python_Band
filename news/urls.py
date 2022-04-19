from django.urls import path
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.news_main, name='main'),
    path('create_news', views.create_news, name='create_news'),

]