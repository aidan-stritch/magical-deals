from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductTests(TestCase):
    """
    Tests for the Product model
    """

    def test_str(self):
        test_name = Product(product_name='Product One')
        self.assertEqual(str(test_name), 'Product One')
