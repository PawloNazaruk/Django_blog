from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'PawloN',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'August 27, 2018'
    },
    {
        'author': 'Wojteg',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'August 28, 2018'
    }
]

Benon = "Beniz"

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def benon(request):
    return HttpResponse('<p>Beniz</p>')


def benon_asd():
    return HttpResponse('<p>asdbeonm</p>')
