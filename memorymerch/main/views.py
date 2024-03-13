from django.shortcuts import render,redirect
from .models import Post,Tovar
from .forms import TovarForm


def index(request):
    context = {
        'tovars': Tovar.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'main/index.html',context)

def about(request):
    return render(request, 'main/about.html')

def rules(request):
    return render(request, 'main/rules.html')

def createtovar(request):
    error = ''
    if request.method == 'POST':
        form = TovarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма заполнена неправильно или не до конца'
    form = TovarForm()
    context = {
        'form': form
    }
    return render(request, 'main/create-tovar.html', context)

def tovar(request):
     return render(request, 'main/tovar.html')