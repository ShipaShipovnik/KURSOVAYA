from django.shortcuts import render
from .models import Post,Tovar

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
