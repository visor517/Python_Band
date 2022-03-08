from django.urls import path

from mainapp.views import main

urlpatterns = [
    path('', main),
    path('index/', main),
    ]
