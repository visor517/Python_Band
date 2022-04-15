# Настроить права доступа!!!

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404

from articleapp.models import Category, Article
from authapp.models import HabrUser
from adminapp.forms import UserRegisterForm, CategoryRegisterForm, ProfileRegisterForm, ArticleRegisterForm, \
    UserUpdateForm


def main(request):
    title = 'Админка'

    context = {
        'title': title,
    }
    return render(request, 'adminapp/admin.html', context=context)


class UserListView(LoginRequiredMixin, ListView):
    model = HabrUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'


# class UserListView(UserPassesTestMixin, ListView):
#     model = HabrUser
#     template_name = 'adminapp/users.html'
#     context_object_name = 'objects'
#
#     def test_func(self):
#         return self.request.user.role('Администратор')


class UserCreateView(LoginRequiredMixin, CreateView):
    model = HabrUser
    form_class = UserRegisterForm
    template_name = 'adminapp/user_create.html'
    success_url = reverse_lazy('_admin:users')


def user_update(request, pk):
    title = 'редактирование'

    edit_user = get_object_or_404(HabrUser, pk=pk)

    if request.method == 'POST':
        edit_form = UserUpdateForm(request.POST, request.FILES, instance=edit_user)
        profile_form = ProfileRegisterForm(request.POST, instance=edit_user.habrprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('_admin:users'))
    else:
        edit_form = UserUpdateForm(instance=edit_user)
        profile_form = ProfileRegisterForm(
            instance=edit_user.habrprofile
        )

    context = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'adminapp/user_update.html', context=context)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = HabrUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('_admin:users')
    context_object_name = 'user_to_delete'


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryRegisterForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('_admin:categories')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryRegisterForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('_admin:categories')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('_admin:categories')
    context_object_name = 'category_to_delete'


class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'adminapp/articles.html'
    context_object_name = 'objects'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleRegisterForm
    template_name = 'adminapp/article_update.html'
    success_url = reverse_lazy('_admin:articles')


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleRegisterForm
    template_name = 'adminapp/article_update.html'
    success_url = reverse_lazy('_admin:articles')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'adminapp/article_delete.html'
    context_object_name = 'article_to_delete'
    success_url = reverse_lazy('_admin:articles')