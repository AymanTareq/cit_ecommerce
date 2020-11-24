from django.shortcuts import render
from .models import *


def all_product(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'essEcommerce/all_product.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , create = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_total_price':0
        }
    context = {
        'order':order,
        'items':items,
    }
    return render(request, 'essEcommerce/cart.html', context)
