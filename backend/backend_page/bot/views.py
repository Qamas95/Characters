from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bot/index.html', context)


def about(request):
    return render(request, 'bot/about.html', {'title': 'About'})