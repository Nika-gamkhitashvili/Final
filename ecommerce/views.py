from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import RegistrationForm
from .models import Product, Cart, CartItem, PurchasedItem


def home(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'main/home.html', {'products': products})


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ecommerce:home-page')
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('ecommerce:home-page')


@login_required
def cards_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    products = CartItem.objects.filter(cart=cart)
    return render(request, 'main/cards.html', {'products': products})


@login_required
def add_to_cart(request, id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=id)
    if product.quantity > 0:
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not cart_item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()
    return redirect('ecommerce:home-page')


@login_required
def remove_from_cart(request, id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=id)
    cart_item = CartItem.objects.filter(Q(cart=cart) & Q(product=product))
    cart_item.delete()
    return redirect('ecommerce:cards')


@login_required
def buy_product(request, id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=id)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        # Create a PurchasedItem entry
        PurchasedItem.objects.create(user=request.user, product=product, quantity=cart_item.quantity)
        # Remove the item from the cart
        cart_item.delete()
    return redirect('ecommerce:cart')


@login_required
def purchased_products(request):
    purchased_items = PurchasedItem.objects.filter(user=request.user)
    return render(request, 'main/purchased_products.html', {'purchased_items': purchased_items})


@login_required
def buy_all_products(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        # Create a PurchasedItem entry for each item in the cart
        PurchasedItem.objects.create(user=request.user, product=cart_item.product, quantity=cart_item.quantity)
        # Remove the item from the cart
        cart_item.delete()
    return redirect('ecommerce:purchased-products')


@login_required
def delete_purchased_product(request, id):
    purchased_item = PurchasedItem.objects.get(id=id, user=request.user)
    purchased_item.delete()
    return redirect('ecommerce:purchased-products')
