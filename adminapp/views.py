#Настроить права доступа!!!

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from articleapp.models import Category
from authapp.models import HabrUser
from adminapp.forms import UserRegisterForm, CategoryEditForm


# def index(request):
#     title = 'Админка'
#
#     context = {
#         'title': title,
#     }
#     return render(request, 'adminapp/admin.html', context=context)


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
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('_admin:users')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = HabrUser
    form_class = UserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('_admin:users')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = HabrUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('_admin:users')
    context_object_name = 'user_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('_admin:categories')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('_admin:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('_admin:categories')
    context_object_name = 'category_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
