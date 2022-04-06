from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('article/', include('articleapp.urls')),
]
