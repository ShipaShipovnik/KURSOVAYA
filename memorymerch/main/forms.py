from .models import Tovar,Categories
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class TovarForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="Категория", required=True)
    class Meta:
        model = Tovar
        fields = ["tovarname", 'tovarprice', 'category', 'shipping', 'tovardescrpt']
        widgets = {
            "tovarname": TextInput(attrs={'placeholder': 'Заголовок товара', 'class': 'form-input'}),
            "tovarprice": TextInput(attrs={'placeholder': 'Цена', 'class': 'form-input'}),
            "category": forms.Select(attrs={'placeholder': 'Категория', 'class': 'form-input'}),
            "shipping": Textarea(attrs={'placeholder': 'Доставка', 'class': 'form-input'}),
            "tovardescrpt": Textarea(attrs={'placeholder': 'Описание', 'class': 'form-input'}),
        }