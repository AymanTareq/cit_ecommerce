from django.shortcuts import render
from .models import *


def all_product(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'essEcommerce/all_product.html', context)
