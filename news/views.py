from django.shortcuts import render
from .models import News


def news_main(request):
    news = News.objects.all()
    return render(request, "news/news_main.html", {'news': news})
