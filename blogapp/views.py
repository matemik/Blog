from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title': 'First post',
        'author': 'Matej',
        'date_posted': '30.08.2019',
        'content': 'This is the first blog post'
    },
    {
        'title': 'Second post',
        'author': 'Matej',
        'date_posted': '30.08.2019',
        'content': 'This is the second blog post'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
