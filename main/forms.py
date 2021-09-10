from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'link', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }
