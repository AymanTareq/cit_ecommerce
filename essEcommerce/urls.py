from django.urls import path
from .views import *

urlpatterns = [
    path('', all_product, name='all-product'),
    path('cart/', cart, name='cart'),
    path('checkout/',check_out, name='check-out'),
    
]
