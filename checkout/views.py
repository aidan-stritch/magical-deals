from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from .forms import Delivery_Person_Form, Delivery_Address_Form
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        user_form = Delivery_Person_Form(request.POST, instance=request.user)
        address_form = Delivery_Address_Form(request.POST,
                                             instance=request.user.usercreate)

        if order_form.is_valid() and payment_form.is_valid() and user_form.is_valid() and address_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            user_form.save()
            address_form.save()

            cart = request.session.get('cart', {})
            total = 0

            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            if customer.paid:
                messages.error(request, "Payment successful")
                request.session['cart'] = {}
                return redirect(reverse('profile'))

            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "Unable to take payment from the card provided")
    else:
        payment_form = MakePaymentForm()
        user_form = Delivery_Person_Form(instance=request.user)
        address_form = Delivery_Address_Form(instance=request.user.usercreate)

    args = {'user_form': user_form, 'address_form': address_form,
            'payment_form': payment_form,
            'publishable': settings.STRIPE_PUBLISHABLE}

    return render(request, "checkout.html", args)
