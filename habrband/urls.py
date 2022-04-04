from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]
