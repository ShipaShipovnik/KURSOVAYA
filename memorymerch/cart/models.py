from django.db import models
from django.contrib.auth.models import User
from main.models import Tovar

class CartItem(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.tovar.name}'
