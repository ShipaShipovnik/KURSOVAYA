from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image


class Categories(models.Model):
    catgname = models.CharField(max_length=60, blank=False, default="")

    def __str__(self):
        return self.catgname


class Tovar(models.Model):
    tovarname = models.CharField(max_length=100, blank=False, default="")
    tovarprice = models.FloatField()
    category = models.ForeignKey(
        "Categories",
        related_name="tovars_categories",
        on_delete=models.CASCADE,
        null=True,
    )
    shipping = models.TextField(max_length=300, blank=False, default="")
    tovardescrpt = models.TextField(max_length=500, blank=False, default="")
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    tovarimage = models.ImageField(
        upload_to="img/tovarimages",
        verbose_name="Фото товара",
        default=None,
        blank=False,
    )

    def __str__(self):
        return f"{self.tovarname} {self.category}"



class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    postbody = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
