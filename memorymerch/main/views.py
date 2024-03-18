from django.shortcuts import render, redirect
from .models import Post, Tovar
from .forms import TovarForm
from .filters import TovarFilter


def index(request):
    tovars_all=Tovar.objects.all(), 
    posts = Post.objects.all()
    filter_tovar= TovarFilter(request.GET, queryset=Tovar.objects.all())
    return render(request, "main/index.html",{'tovars':filter_tovar,'posts':posts})


def about(request):
    return render(request, "main/about.html")


def rules(request):
    return render(request, "main/rules.html")


def createtovar(request):
    error = ""
    if request.method == "POST":
        form = TovarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            error = "Форма заполнена неправильно или не до конца"
    form = TovarForm()
    context = {"form": form}
    return render(request, "main/create-tovar.html", context)


def tovar(request):
    return render(request, "main/tovar.html")
