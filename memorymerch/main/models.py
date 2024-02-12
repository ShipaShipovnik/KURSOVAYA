from django.db import models


class Categories(models.Model):
    catgname = models.CharField(max_length=60, blank=False, default='')


class Tovar(models.Model):
    tovarname = models.CharField(max_length=100, blank=False, default='')
    tovarprice = models.FloatField()
    category = models.ForeignKey('Categories', related_name='tovars_categories', on_delete=models.CASCADE)
    shipping = models.TextField(max_length=300, blank=False, default='')
    tovardescrpt = models.TextField(max_length=500, blank=False, default='')


