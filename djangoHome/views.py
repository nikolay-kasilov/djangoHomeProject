from django.shortcuts import render
from .models import Articles



def index(request):
    return  render(request,'text/index.html',{'title':'Главная страница'})


def about(request):
    return render(request, 'text/about.html')


def new(request):
    return  render(request,'text/new.html')

def new_home(request):
    news = Articles.objects.all()
    return render(request,'news/news_home.html',{'news':news})