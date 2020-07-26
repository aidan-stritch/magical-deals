from django import forms
from .models import Order


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
        fields = ('name', 'phone_Number',
                  'address_Line_One', 'address_Line_Two',
                  'address_Line_Three', 'town_or_City',
                  'county', 'postcode', 'country')
