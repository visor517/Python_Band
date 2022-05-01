from django.shortcuts import render
from articleapp.models import Article
from django.db.models import Q


def search(request):
    """
    Поиск по сайту
    :param request:
    :return:
    """
    if request.method == "POST":
        searched = request.POST['searched']
        results = Article.objects.filter(
            Q(content__icontains=searched) | Q(title__icontains=searched) |
            Q(author__username__icontains=searched))
        return render(request, 'search.html',
                      {'searched': searched,
                       'results': results})
    else:
        return render(request, 'search.html',
                      {})
