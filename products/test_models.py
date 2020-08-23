from django.test import TestCase
from .models import Product


# tests for the models in the products app
class ProductModelTests(TestCase):
    """
    Tests for the UserCreate model
    """
    def test_str(self):

        product_name = Product(product_name='test')
        description = Product(description='this is a test')
        price = Product(price='13.22')
        image = Product(image='test.jpg')
        rating = Product(rating='5')

        self.assertEqual(str(product_name.product_name), 'test')
        self.assertEqual(str(description.description), 'this is a test')
        self.assertEqual(str(price.price), '13.22')
        self.assertEqual(str(image.image), 'test.jpg')
        self.assertEqual(str(rating.rating), '5')
