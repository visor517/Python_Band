from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.MainView.as_view(), name='main_admin'),
    path('users/', adminapp.UserListView.as_view(), name='users'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/', adminapp.CategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    path('articles/create/', adminapp.ArticleCreateView.as_view(), name='article_create'),
    path('articles/', adminapp.ArticlesListView.as_view(), name='articles'),
    path('articles/update/<uuid:pk>/', adminapp.ArticleUpdateView.as_view(), name='article_update'),
    path('articles/delete/<uuid:pk>/', adminapp.ArticleDeleteView.as_view(), name='article_delete'),
]
