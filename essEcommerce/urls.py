from django.urls import path
from .views import *

urlpatterns = [
    path('', all_product, name='all-product'),
    path('cart/', cart, name='cart'),
]
