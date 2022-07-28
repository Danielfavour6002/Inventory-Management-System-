from operator import mod
from attr import fields
from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class OrderStatus(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']