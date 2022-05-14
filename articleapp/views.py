from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,\
    DeleteView
from django.views.generic.edit import FormMixin
from articleapp.forms import ArticleForm, ArticleApprove
from articleapp.models import Article, Like, Category
from commentapp.forms import CommentsForm
from commentapp.views import CommentView
from mainapp.views import main
from .mixins import UserIsNoBlockMixin


# Отображение содержимого из модели Article
class IndexView(ListView):
    """
    класс - Index
    """
    model = Article
    paginate_by = 3
    template_name = 'mainapp/index.html'


# Отображение списка статей
class ArticleListView(ListView):
    """
    класс - ArticleList
    """
    model = Article
    paginate_by = 5
    template_name = 'articles_list.html'

    def get_queryset(self):
        """
        :return:
        """
        return Article.objects.filter(author=self.request.user)


# Отображение содержимого
class ArticleDetailView(CommentView, FormMixin, DetailView):
    """
    класс - ArticleDetail
    """
    model = Article
    form_class = CommentsForm
    second_form_class = ArticleApprove
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(instance=self.object.comments)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.object)
        return context

    # Убрал форму апрува статьи, так как при создании нового коммента статья отправляется на модерацию
    # Не понимаю назначения этого действия!!
    # def post(self, request, *args, **kwargs):
    #     """
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     self.object = self.get_object()
    #     form2 = self.second_form_class(request.POST, instance=self.object)
    #     if form2.is_valid():
    #         form2.save()
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return self.render_to_response(
    #             self.get_context_data(form2=form2))


class ArticleCreateView(CreateView):

    """
    класс - ArticleCreate
    """
    model = Article
    template_name = 'article_new.html'
    form_class = ArticleForm

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.get_form()
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            self.object = article.save()
            return redirect('auth:profile', request.user.pk)

        return self.form_invalid(form)


class ArticleUpdateView(UserIsNoBlockMixin, UpdateView):
    """
    класс - ArticleUpdate
    """
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'category', 'content', 'image']


class ArticleDeleteView(UserIsNoBlockMixin, DeleteView):
    """
    класс - ArticleDelete
    """
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy(main)


class ArticlePublished(UserIsNoBlockMixin, DeleteView):
    """
    класс - Публикация статьи
    """
    model = Article

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

    def delete(self, request, *args, **kwargs):
        """  """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'PB'
        self.object.save()
        return HttpResponseRedirect(success_url)


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

        data = {
            'value': like.value,
            'likes': article_obj.liked.all().count()
        }
        return JsonResponse(data, safe=False)

    return redirect('article:detail', pk=pk)


class CategoryArticleView(ListView):
    """
    класс - Сортировка статей по категориям
    """
    model = Article
    template_name = 'category.html'
    paginate_by = 6

    def get_queryset(self):
        """
        :return:
        """
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Article.objects.filter(category=self.category)\
            .filter(status='PB', approve=True)

    def get_context_data(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        context = super(CategoryArticleView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
