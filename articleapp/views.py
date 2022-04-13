from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from articleapp.forms import ArticleForm
from articleapp.models import Article
from mainapp.views import main


# Отображение содержимого из модели Article
class ArticleListView(ListView):
    model = Article
    template_name = 'mainapp/index.html'


# Отображение содержимого
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    form_class = ArticleForm


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    form_class = ArticleForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            self.object = article.save()
            return redirect(article)

        return self.form_invalid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'category', 'content', 'image']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy(main)

# Create your views here.
