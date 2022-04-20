from django.shortcuts import render


def main(request):
    title = "Main"

    content = {"title": title}

    return render(request, "mainapp/index.html", content)

