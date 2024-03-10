from django.shortcuts import render
from djangoHome.models import Articles
from  djangoHome.forms import ArticlesForm

def news_home(request):
    news =Articles.objects.all()
    return render(request,'news/news.html',{'news':news})
def create(request):
    form = ArticlesForm()
    date={
        'form': form
    }
    return render(request,'news/create.html', date)

