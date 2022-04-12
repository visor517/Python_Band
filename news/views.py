from django.shortcuts import render


def news_main(request):
    return render(request, "news/news_main.html")


