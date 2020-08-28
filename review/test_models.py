from django.test import TestCase
from .models import Review
from django.contrib.auth.models import User
from products.models import Product


# tests for the model in the review app
class ReviewModelTests(TestCase):
    """Tests for the Review model."""
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='whosthedoctor@gallifrey.com',
            username='TheDoctor',
            password='tardis',
            first_name='Doctor',
            last_name='Who'
        )

    def test_str(self):
        test_product = Product(
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )

        self.client.login(username='TheDoctor', password='tardis')

        product = Review(product=test_product)
        description = Review(description='This is a description')
        rating = Review(rating='7')

        self.assertEqual(str(product.product), 'testproduct')
        self.assertEqual(str(description.description), 'This is a description')
        self.assertEqual(str(rating.rating), '7')
