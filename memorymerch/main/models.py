from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Categories(models.Model):
    catgname = models.CharField(max_length=60, blank=False, default='')

    def __str__(self):
        return self.catgname


class Tovar(models.Model):
    tovarname = models.CharField(max_length=100, blank=False, default='')
    tovarprice = models.FloatField()
    category = models.ForeignKey('Categories', related_name='tovars_categories', on_delete=models.CASCADE,null = True)
    shipping = models.TextField(max_length=300, blank=False, default='')
    tovardescrpt = models.TextField(max_length=500, blank=False, default='')
    date_posted = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return f'{self.tovarname} {self.category}'


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    postbody = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.tovar.tovarname}'
