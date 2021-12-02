from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartProduct

from django.http import HttpResponse


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id, add=None):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartProduct.objects.get(product=product, cart=cart)
        if add == 0 and cart_item.quantity < 10 and product.stock > cart_item.quantity:
            cart_item.quantity += 1
        elif add == 1 and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
    except CartProduct.DoesNotExist:
        cart_item = CartProduct.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()

    return redirect('cart')


def cart(request):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartProduct.objects.filter(cart=cart, is_active=True)
    except:
        pass

    context = {
        'cart_item': cart_item
    }

    return render(request, 'store/cart.html', context)
