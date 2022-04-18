from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect

from articleapp.models import Category, Article
from authapp.models import HabrUser
from adminapp.forms import UserRegisterForm, CategoryRegisterForm, ProfileRegisterForm, ArticleRegisterForm, \
    UserUpdateForm


class UserIsAdminMixin(UserPassesTestMixin):
    """ Предоставляет право доступа пользователю у которого роль Администратор """
    def test_func(self):
        return self.request.user.role == 'A'

    def handle_no_permission(self):
        return redirect('/')


class UserIsPersonalMixin(UserPassesTestMixin):
    """ Предоставляет право доступа пользователю у которого роль Администратор или Модератор"""
    def test_func(self):
        return self.request.user.role != 'U'

    def handle_no_permission(self):
        return redirect('/')


class MainView(LoginRequiredMixin, UserIsPersonalMixin, TemplateView):
    template_name = 'adminapp/admin.html'


class UserListView(LoginRequiredMixin, UserIsPersonalMixin, ListView):
    model = HabrUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'


class UserCreateView(LoginRequiredMixin, UserIsAdminMixin, CreateView):
    model = HabrUser
    form_class = UserRegisterForm
    template_name = 'adminapp/user_create.html'
    success_url = reverse_lazy('_admin:users')


class UserUpdateView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    model = HabrUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('_admin:users')
    form_class = UserUpdateForm
    second_form_class = ProfileRegisterForm

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(instance=self.object)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.object.habrprofile)
        context['avatar'] = self.object.avatar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form2 = self.second_form_class(request.POST, instance=self.object.habrprofile)
        form2.save()
        return super().post(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, UserIsPersonalMixin, DeleteView):
    model = HabrUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('_admin:users')
    context_object_name = 'user_to_delete'


class CategoryListView(LoginRequiredMixin, UserIsAdminMixin, ListView):
    model = Category
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


class CategoryCreateView(LoginRequiredMixin, UserIsAdminMixin, CreateView):
    model = Category
    form_class = CategoryRegisterForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('_admin:categories')


class CategoryUpdateView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    model = Category
    form_class = CategoryRegisterForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('_admin:categories')


class CategoryDeleteView(LoginRequiredMixin, UserIsAdminMixin, DeleteView):
    model = Category
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('_admin:categories')
    context_object_name = 'category_to_delete'


class ArticlesListView(LoginRequiredMixin, UserIsPersonalMixin, ListView):
    model = Article
    template_name = 'adminapp/articles.html'
    context_object_name = 'objects'


class ArticleCreateView(LoginRequiredMixin, UserIsPersonalMixin, CreateView):
    model = Article
    form_class = ArticleRegisterForm
    template_name = 'adminapp/article_update.html'
    success_url = reverse_lazy('_admin:articles')


class ArticleUpdateView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    model = Article
    form_class = ArticleRegisterForm
    template_name = 'adminapp/article_update.html'
    success_url = reverse_lazy('_admin:articles')


class ArticleDeleteView(LoginRequiredMixin, UserIsPersonalMixin, DeleteView):
    model = Article
    template_name = 'adminapp/article_delete.html'
    context_object_name = 'article_to_delete'
    success_url = reverse_lazy('_admin:articles')