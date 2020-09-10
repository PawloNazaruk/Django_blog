from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


Benon = "Beniz"


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def benon(request):
    return HttpResponse('<p>Beniz</p>')


def benon_asd():
    return HttpResponse('<p>asdbeonm</p>')
