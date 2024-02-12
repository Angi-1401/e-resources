from django.shortcuts import render

from apps.library.models import Collection


def index(request):
    collections = Collection.objects.all()
    context = {"collections": collections}

    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
