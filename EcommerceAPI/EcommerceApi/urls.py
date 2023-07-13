from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-view'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('addCart/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(), name='cart-view'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]