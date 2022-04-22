from django.shortcuts import render
from articleapp.models import Article
from django.db.models import Q

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Article.objects.filter(
            Q(content__contains=searched) | Q(title__contains=searched))
        return render(request, 'search.html',
                      {'searched': searched,
                       'results': results})
    else:
        return render(request, 'search.html',
                      {})
