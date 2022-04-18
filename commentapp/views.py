from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# from articleapp.models import Article
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class SuccessMessage:
    """
    класс - Оповещение
    """
    def success_msg(self):
        """
        :return:
        """
        return False

    def form_valid(self, form):
        """
        :param form:
        :return:
        """
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        """
        :return:
        """
        return '%s?id=%s' % (self.success_url, self.object.id)


class CommentView(SuccessMessage):
    """
    класс - CommentView
    """
    success_msg = 'Комментарий создан и отправлен на модерацию.'

    def get_success_url(self, **kwargs):
        """
        :param self:
        :param kwargs:
        :return:
        """
        return reverse_lazy('articleapp:detail',
                            kwargs={'pk': self.get_object().uid})

    def post(self, request, *args, **kwargs):
        """
        :param self:
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        :param self:
        :param form:
        :return:
        """
        self.object = form.save(commit=False)
        self.object.comment_article = self.get_object()
        self.object.comment_author = self.request.user
        self.object.save()
        return super().form_valid(form)


# class AddLike(LoginRequiredMixin, View):
#     """
#     класс - Поставить лайк
#     """
#     def article(self, request, pk, *args, **kwargs):
#         """
#         :param request:
#         :param pk:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         article = Article.objects.get(pk=pk)
#
#         is_dislike = False
#
#         for dislike in article.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break
#
#         if is_dislike:
#             article.dislikes.remove(request.user)
#
#         is_like = False
#
#         for like in article.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break
#
#         if not is_like:
#             article.likes.add(request.user)
#         if is_like:
#             article.likes.remove(request.user)
#
#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)
#
#
# class Dislike(LoginRequiredMixin, View):
#     """
#     класс - Поставить дизлайк
#     """
#     def article(self, request, pk, *args, **kwargs):
#         """
#         :param request:
#         :param pk:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         article = Article.objects.get(pk=pk)
#
#         is_like = False
#
#         for like in article.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break
#
#         if is_like:
#             article.likes.remove(request.user)
#
#         is_dislike = False
#
#         for dislike in article.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break
#
#         if not is_dislike:
#             article.dislikes.add(request.user)
#         if is_dislike:
#             article.dislikes.remove(request.user)
#
#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)
