from django.urls import path
from . import views
from .views import TovarDetail,TovarList

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('rules', views.rules, name='rules'),
    path('create-tovar', views.createtovar, name='create-tovar'),
    path('tovar/', TovarList.as_view(),name='tovars'),
    path('tovar/<int:pk>/', TovarDetail.as_view(), name='tovar'),
    path('basket',views.basket,name='basket'),
    path('basket-add/<int:tovar_id>', views.basket_add,name="basket-add")
]
