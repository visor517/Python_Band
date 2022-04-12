from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temp/', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('news/', include('news.urls', namespace='news')),
    path('', include('articleapp.urls', namespace='article')),

]
