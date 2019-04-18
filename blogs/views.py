from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template import loader
# Create your views here.

def index(request):
    return render(request, 'blogs/index.html')

def add(request):
    return render(request, 'blogs/index.html')

def detail(request, article_id):
    list = Article.objects.get(id=1)
    template = loader.get_template('blogs/index.html')
    context = {'list':list}
    return render(request, 'blogs/index.html')

