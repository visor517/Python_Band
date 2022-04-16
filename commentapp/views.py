from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .models import Comments
from django.http import HttpResponseRedirect


class CommentView:
    """
    класс - CommentView
    """

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


def comment_like_view(request, pk):
    """
    :param request:
    :return:
    """
    comments = get_object_or_404(Comments,
                                 id=request.POST.get('comments_id'))
    comments.likes.add(request.user)
    return HttpResponseRedirect(reverse('articleapp:detail',
                                        args=[str(pk)]))
