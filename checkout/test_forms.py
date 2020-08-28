from django.test import TestCase
from .forms import MakePaymentForm


# tests for the forms in the checkout app.
class FormIsValidTests(TestCase):
    """Tests to ensure forms are valid."""

    def test_make_payment_form_is_valid(self):
        test_form = MakePaymentForm({'credit_card_number': '4242424242424242',
                                     'cvv': '111', 'expiry_month': '11',
                                     'expiry_year': '2050', 'stripe_id': '1'})

        self.assertTrue(test_form.is_valid())
