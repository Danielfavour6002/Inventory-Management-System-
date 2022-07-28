from django.contrib import admin

from .models import Product, Order
admin.site.site_header = 'BusYem Inventory'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)


    
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

# Register your models here.

# 100%Yemi1, password, 100%Temilola1
# Busayo, admin