from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from articleapp.models import Article


def main(request):
    title = "Main"

    content = {"title": title}

    return render(request, "mainapp/index.html", content)


# Отображение содержимого из модели Article
class ArticleListView(ListView):
    model = Article
    template_name = 'mainapp/index.html'


# Отображение содержимого
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'mainapp/article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'mainapp/article_new.html'
    fields = ['title', 'author', 'category', 'content', 'image']


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'mainapp/article_edit.html'
    fields = ['title', 'category', 'content', 'image']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'mainapp/article_delete.html'
    success_url = reverse_lazy(main)
