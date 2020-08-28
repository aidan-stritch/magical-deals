from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def view_cart(request):
    """View renders the cart contents page."""
    return render(request, "cart.html")


def add_to_cart(request, pk):
    """Adds a quantity of the specified product to the cart."""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[pk] = quantity
    else:
        cart[pk] = cart.get(pk, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, pk):
    """This will be used to adjust the quantity
    of the specified product to the specified amount."""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[pk] = quantity
    else:
        cart.pop(pk)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def empty_cart(request):
    request.session['cart'] = {}
    messages.success(request, "Cart successfully emptied")
    return redirect(reverse('index'))

