from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Post, Tovar, Basket
from .forms import TovarForm
from .filters import TovarFilter
from django.views.generic import DetailView, ListView


def index(request):
    tovars_all = (Tovar.objects.all(),)
    posts = Post.objects.all()
    filter_tovar = TovarFilter(request.GET, queryset=Tovar.objects.all())
    return render(request, "main/index.html", {"tovars": filter_tovar, "posts": posts})


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


class TovarList(ListView):
    model = Tovar
    context_object_name = "tovars"


class TovarDetail(DetailView):
    model = Tovar
    template_name = "main/tovar.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def basket_add(request, tovar_id):
    current_page = request.META.get("HTTP_REFERER")
    tovar = Tovar.objects.get(id=tovar_id)
    baskets = Basket.objects.filter(user=request.user, tovar=tovar)

    if not baskets.exists():
        Basket.objects.create(user=request.user, tovar=tovar, quantity=1)
        # basket = Basket(user=request.user, tovar = tovar,quantity = 1)
        # basket.save()
        return HttpResponseRedirect(current_page)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)

def basket(request):
    if request.user.is_authenticated:
        context = {"baskets": Basket.objects.filter(user=request.user)}
        return render(request, "main/basket.html", context)
    else:
        return render(request, "account/signup.html")

    
