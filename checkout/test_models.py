from django.test import TestCase
from .models import Order
from django.contrib.auth.models import User


class CheckoutModelTests(TestCase):
    """Tests for the checkout models."""

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='whosthedoctor@gallifrey.com',
            username='TheDoctor',
            password='tardis',
            first_name='Doctor',
            last_name='Who'
        )

    def test_order_fields(self):
        phone_Number = Order(phone_Number='5550135')
        address_Line_One = Order(address_Line_One='testadd1')
        address_Line_Two = Order(address_Line_Two='testadd2')
        address_Line_Three = Order(address_Line_Three='testadd3')
        town_or_City = Order(town_or_City='testcity')
        county = Order(county='testcounty')
        postcode = Order(postcode='testpostcode')
        country = Order(country='testcountry')
        date = Order(date='11/11/2025')

        self.assertEqual(str(phone_Number.phone_Number),
                         '5550135')
        self.assertEqual(str(address_Line_One.address_Line_One),
                         'testadd1')
        self.assertEqual(str(address_Line_Two.address_Line_Two),
                         'testadd2')
        self.assertEqual(str(address_Line_Three.address_Line_Three),
                         'testadd3')
        self.assertEqual(str(town_or_City.town_or_City),
                         'testcity')
        self.assertEqual(str(county.county),
                         'testcounty')
        self.assertEqual(str(postcode.postcode),
                         'testpostcode')
        self.assertEqual(str(country.country),
                         'testcountry')
        self.assertEqual(str(date.date),
                         '11/11/2025')
