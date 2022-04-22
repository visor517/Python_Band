from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.generic.edit import FormMixin
from commentapp.forms import CommentsForm
from commentapp.views import CommentView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from articleapp.forms import ArticleForm
from articleapp.models import Article
from mainapp.views import main


# Отображение содержимого из модели Article
class ArticleListView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'mainapp/index.html'


# Отображение содержимого
class ArticleDetailView(CommentView, FormMixin, DetailView):
    model = Article
    form_class = CommentsForm
    template_name = 'article_detail.html'
    # form_class = ArticleForm


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


class AddLike(LoginRequiredMixin, View):
    """
    класс - Поставить лайк
    """
    def article(self, request, pk, *args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        article = Article.objects.get(pk=pk)

        is_dislike = False

        for dislike in article.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            article.dislikes.remove(request.user)

        is_like = False

        for like in article.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            article.likes.add(request.user)
        if is_like:
            article.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class Dislike(LoginRequiredMixin, View):
    """
    класс - Поставить дизлайк
    """
    def article(self, request, pk, *args, **kwargs):
        """
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        article = Article.objects.get(pk=pk)

        is_like = False

        for like in article.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            article.likes.remove(request.user)

        is_dislike = False

        for dislike in article.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            article.dislikes.add(request.user)
        if is_dislike:
            article.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
