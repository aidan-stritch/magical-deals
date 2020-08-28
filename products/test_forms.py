from django.test import TestCase
from products.forms import ProductCreationForm


# tests for the forms in the accounts app.
class ProductCreationFormTests(TestCase):
    """Tests for the products app ProductCreationForm form."""
    def test_form_invalid_with_empty_fields(self):
        product = ProductCreationForm({'product_name': '',
                                       'description': '',
                                       'price': '',
                                       'image': ''})
        self.assertFalse(product.is_valid())

