from django.test import TestCase
from django.contrib.auth.models import User
from .forms import MakePaymentForm, OrderForm
from .forms import Delivery_Person_Form, Delivery_Address_Form
from django.utils import timezone


# tests for the views in the checkout app.
class ViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='whosthedoctor3@gallifrey.com',
            username='TheDoctor3',
            password='tardis',
            first_name='Doctor3',
            last_name='Who'
        )

    def test_get_checkout_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')

        payment_form = MakePaymentForm()
        user_form = Delivery_Person_Form()
        address_form = Delivery_Address_Form()
        publishable = "test"

        args = {'user_form': user_form, 'address_form': address_form,
                'payment_form': payment_form,
                'publishable': publishable}

        page = self.client.get('/checkout/', args)

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "checkout.html")

    def test_checkout_forms_are_valid(self):
        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')

        order_form = OrderForm('')
        payment_form = MakePaymentForm({'credit_card_number':
                                        '4242424242424242',
                                        'cvv': '111',
                                        'expiry_month': '11',
                                        'expiry_year': '2050',
                                        'stripe_id': '1'})
        user_form = Delivery_Person_Form({'first_name': 'testname',
                                          'last_name': 'testlast'})
        address_form = Delivery_Address_Form({'add_Line_One': 'testaddress1',
                                              'add_Line_Two': 'testaddress2',
                                              'add_Line_Three': 'testaddress3',
                                              'city': 'testcity',
                                              'country': 'testcountry',
                                              'postcode': 'testpostcode',
                                              'phone': '5551235'})

        if order_form.is_valid() and payment_form.is_valid():
            if user_form.is_valid() and address_form.is_valid():
                order = order_form.save(commit=False)
                order.user = user
                order.date = timezone.now()

                user_form.save()
                order_form.save()

        self.assertTrue(order_form.is_valid())
        self.assertTrue(payment_form.is_valid())
        self.assertTrue(user_form.is_valid())
        self.assertTrue(address_form.is_valid())
        self.assertTrue(user_form.save())
        self.assertTrue(order_form.save())
