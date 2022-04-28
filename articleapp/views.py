from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.views.generic.edit import FormMixin
from commentapp.forms import CommentsForm
from commentapp.views import CommentView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from articleapp.forms import ArticleForm
from articleapp.models import Article, Like
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


def like_art(request, pk):
    """
    :param request:
    :param pk:
    :return:
    """
    user = request.user
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        article_obj = Article.objects.get(pk=article_id)

        if user in article_obj.liked.all():
            article_obj.liked.remove(user)
        else:
            article_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user,
                                                   article_id=article_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Dislike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            article_obj.save()
            like.save()

    return redirect('article:detail', pk=pk)
