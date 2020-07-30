from django import forms
from .models import Order
from django.contrib.auth.models import User
from accounts.models import UserCreate


class MakePaymentForm(forms.Form):
    """ a form that takes the payment
    information from the customer"""

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2099)]

    credit_card_number = forms.CharField(
        label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Card (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """ a form that shows the order
    the customer is purchasing using the Order model"""
    class Meta:
        model = Order
        fields = ()


class Delivery_Person_Form(forms.ModelForm):
    """ a form that displays the users name
    for delivery address purposes"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class Delivery_Address_Form(forms.ModelForm):
    """ a form that displays the users address
    for delivery address purposes"""
    class Meta:
        model = UserCreate
        fields = ('address_line_one', 'address_line_two',
                  'address_line_three', 'city', 'country', 'postcode',
                  'phone')
