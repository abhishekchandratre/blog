from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('portfolio/index.html')
    return render(request, 'portfolio/index.html', context)

def blog(request):
    context = {}
    template = loader.get_template('portfolio/blogs.html')
    return render(request, 'portfolio/blogs.html', context)

def about_me(request):
    context = {}
    template = loader.get_template('portfolio/about_me.html')
    return render(request, 'portfolio/about_me.html', context)

def projects(request):
    context = {}
    template = loader.get_template('portfolio/projects.html')
    return render(request, 'portfolio/projects.html', context)

def links(request):
    context = {}
    template = loader.get_template('portfolio/links.html')
    return render(request, 'portfolio/links.html', context)

