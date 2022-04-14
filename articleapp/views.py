from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from commentapp.forms import CommentsForm
from commentapp.views import CommentView

from articleapp.models import Article
from mainapp.views import main


# Отображение содержимого из модели Article
class ArticleListView(ListView):
    model = Article
    template_name = 'mainapp/index.html'


# Отображение содержимого
class ArticleDetailView(CommentView, FormMixin, DetailView):
    model = Article
    form_class = CommentsForm
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'author', 'category', 'content', 'image']


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'category', 'content', 'image']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy(main)


from django.shortcuts import render

# Create your views here.
