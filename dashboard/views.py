from itertools import count
from math import prod
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import dashboard
from .models import Product, Order
from .forms import ProductForm, OrderForm, OrderStatus
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required(login_url= 'user-login')
def index(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    products = Product.objects.all()
    product_count = products.count()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance =  form.save(commit = False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'products': products,
        'form' : form,
        'orders_count' : orders_count,
        'workers_count': workers_count,
        'product_count': product_count
      

    }
    return render(request,'dashboard/index.html', context)
    
@login_required(login_url= 'user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = User.objects.all().count()
    product_count = User.objects.all().count()
    context ={
        'workers' : workers,
        'workers_count': workers_count,
        'orders_count' : orders_count,
        'product_count': product_count
    }
    return render(request,'dashboard/staff.html', context)


@login_required(login_url= 'user-login')
def product(request):
    items = Product.objects.all()
    workers_count = User.objects.all().count()
    orders_count = User.objects.all().count()
    product_count = items.count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form': form,
        'workers_count': workers_count,
        'orders_count' : orders_count,
        'product_count': product_count
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url= 'user-login')
def staff_details(request, pk):
    workers = User.objects.get(id=pk)
    
    
    context = {
        'workers' : workers,
        
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url= 'user-login')
def order(request):
    orders = Order.objects.all()
    workers_count = User.objects.all().count()
    orders_count = orders.count()
    product_count = User.objects.all().count()


    context = {
        'orders' : orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,

       
    }

    return render(request, 'dashboard/order.html', context)

def product_delete(request, pk):
    item =Product.objects.get(id =pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def order_delete(request, pk):
    item =Order.objects.get(id =pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-order')
    return render(request, 'dashboard/order_delete.html')

@login_required(login_url= 'user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)

    context = {
        'form' : form,
    }
    return render(request, 'dashboard/product_update.html', context)

def order_status(request, pk):
    items = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        form = OrderStatus(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('dashboard-order')
    else:
        form = OrderStatus(instance=items)

    context = {
        'form' : form,
    }

    return render(request, 'dashboard/order_status.html', context  )