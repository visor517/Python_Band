from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temp/', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('', include('articleapp.urls', namespace='article')),
    path('', include('social_django.urls', namespace='social')),
    path('', include('commentapp.urls', namespace='comment')),
]
