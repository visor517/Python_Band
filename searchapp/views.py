from django.shortcuts import render
from articleapp.models import Article
from django.db.models import Q
from commentapp.models import Comments
from authapp.models import HabrUser


def search(request):
    """
    Поиск по сайту
    :param request:
    :return:
    """
    if request.method == "POST":
        searched = request.POST['searched']
        results = Article.objects.filter(
            Q(content__contains=searched) | Q(title__contains=searched) |
            Q(author__username__contains=searched))
        results_2 = Comments.objects.filter(
            Q(comment_author__username__contains=searched) |
            Q(comment_text__contains=searched))
        results_3 = HabrUser.objects.filter(
            Q(username__contains=searched))
        return render(request, 'search.html',
                      {'searched': searched,
                       'results': results,
                       'results_2': results_2,
                       'results_3': results_3})
    else:
        return render(request, 'search.html',
                      {})
