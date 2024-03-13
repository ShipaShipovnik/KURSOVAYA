from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('rules', views.rules, name='rules'),
    path('create-tovar', views.createtovar, name='create-tovar'),
    path('tovar', views.tovar, name='tovar'),

]
