from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def detail(request, article_id):
    list = Article.objects.get(id=1)
    template = loader.get_template('blogs/index.html')
    context = {'list':list}
    return HttpResponse(template.render(context,request))

