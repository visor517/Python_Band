from django.contrib import admin
from articleapp.models import Category, Article

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)