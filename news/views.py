from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


def news_main(request):
    news = News.objects.order_by('-date')
    return render(request, "news/news_main.html", {'news': news})


def create_news(request):
    error = ''
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news:main')
        else:
            error = "Ошибка вводда данных"
    form_news = NewsForm()
    data = {
        'form': form_news,
        'error': error
    }
    return render(request, "news/create_news.html", data)
