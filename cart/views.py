from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


@login_required
def view_cart(request):
    """ this view renders the cart contents page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ adds a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """ this will be used to adjust the quantity
    of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def empty_cart(request):
    request.session['cart'] = {}
    messages.success(request, "Cart successfully emptied")
    return redirect(reverse('index'))
