from django.contrib import admin
from .models import Tovar, Post, Categories,Basket

admin.site.register(Tovar)
admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Basket)
