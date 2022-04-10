from django.urls import path

from .views import login, logout, register, edit, verify
from django.conf.urls import include, url

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('verify/<email>/<activation_key>', verify, name="verify"),
]
