from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'firstname':'Abhishek'}
    template = loader.get_template('portfolio/index.html')
    return render(request, 'portfolio/index.html', context)

def about_me(request):
    return HttpResponse("Hello world you are at portifolio")
