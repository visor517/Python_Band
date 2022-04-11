from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_admin/', include('adminapp.urls', namespace='_admin')),
    path('temp/', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('', include('articleapp.urls', namespace='article')),
]
