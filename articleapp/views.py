from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from articleapp.forms import ArticleForm, ArticleApprove
from articleapp.models import Article, Category, IpModel
from commentapp.forms import CommentsForm
from commentapp.views import CommentView
from mainapp.views import main


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


def get_user_ip(request):
    """
    :param request:
    :return:
    """
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded:
        ip = forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.object = self.get_object()
        form2 = self.second_form_class(request.POST, instance=self.object)
        if form2.is_valid():
            form2.save()
            return super().post(request, *args, **kwargs)
        else:
            return self.render_to_response(
                self.get_context_data(form2=form2))

    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        like_status = False
        ip = get_user_ip(request)
        if self.object.liked.filter(id=IpModel.objects.get(ip=ip).id).exists():
            like_status = True
        else:
            like_status = False
        context['like_status'] = like_status

        return self.render_to_response(context)


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
            return redirect('article:list')

        return self.form_invalid(form)


class ArticleUpdateView(UpdateView):
    """
    класс - ArticleUpdate
    """
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'category', 'content', 'image']


class ArticleDeleteView(DeleteView):
    """
    класс - ArticleDelete
    """
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy(main)

# Create your views here.

def like_art(request, pk):
    """
    :param request:
    :param pk:
    :return:
    """
    article_id = request.POST.get('article_id')
    article = Article.objects.get(pk=article_id)
    ip = get_user_ip(request)
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if article.liked.filter(id=IpModel.objects.get(ip=ip).id).exists():
        article.liked.remove(IpModel.objects.get(ip=ip))
    else:
        article.liked.add(IpModel.objects.get(ip=ip))
    return HttpResponseRedirect(reverse('article:detail', args=[article_id]))


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
            .filter(status='PB')

    def get_context_data(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        context = super(CategoryArticleView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
