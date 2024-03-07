from django.urls import path ,include
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('about', views.about),
    path('new', views.new)
    ]