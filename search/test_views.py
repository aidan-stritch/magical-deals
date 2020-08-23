from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User


# tests for the view in the search app.
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

    def test_get_search_view_success(self):
        test_product = Product(
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )

        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')

        page = self.client.get('/products/', {"test_product": test_product})

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "products.html")
