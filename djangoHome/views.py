from django.shortcuts import render
from .models import Articles



def index(request):
    data ={
        'title': 'Главная страница',
        'values':['<h1>jhhbbg</h1>']
    }
    return  render(request,'text/index.html' , data)


def about(request):
    return render(request, 'text/about.html')


def new(request):
    return  render(request,'text/new.html')

