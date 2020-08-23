from django.test import TestCase
from products.forms import ProductCreationForm


# tests for the forms in the accounts app.
class ProductCreationFormTests(TestCase):
    """
    Tests for the products app ProductCreationForm form
    """
    def test_form_invalid_with_empty_fields(self):
        product = ProductCreationForm({'product_name': '',
                                       'description': '',
                                       'price': '',
                                       'image': ''})
        self.assertFalse(product.is_valid())

    def test_can_save_with_valid_form(self):
        product = ProductCreationForm({'product_name': 'formtestagain',
                                       'description': 'this is a test',
                                       'price': '8',
                                       'image': 'test.jpg'})
        product.save()

        self.assertTrue(product.is_valid())
        self.assertTrue(product.save())

