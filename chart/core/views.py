from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)

def line(request):
    return render(request, 'line.html')

def pie(request):
    return render(request, 'pie.html')

def XY(request):
    return render(request, 'XY.html')

def map(request):
    return render(request, 'map.html')

def candlesticks(request):
    return render(request, 'candlesticks.html')

def stock(request):
    return render(request, 'stock.html')

def pyramid(request):
    return render(request, 'pyramid.html')

def miscellaneous(request):
    return render(request, 'miscellaneous.html')



