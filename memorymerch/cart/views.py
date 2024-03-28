from django.shortcuts import render, redirect, HttpResponse
from .models import CartItem
from main.models import Tovar


def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.tovar.tovarprice * item.quantity for item in cart_items)
        return render(
            request,
            "cart/cart.html",
            {"cart_items": cart_items, "total_price": total_price},
        )
    else:
        return render(request, "account/signup.html")


def add_to_cart(request, tovar_id):
    tovar = Tovar.objects.get(id=tovar_id)
    cart_item, created = CartItem.objects.get_or_create(tovar=tovar, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart:view_cart")


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect("cart:view_cart")
