from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/<int:add>/', views.add_to_cart, name='add_cart')
]
