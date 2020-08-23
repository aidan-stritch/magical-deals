from django.test import TestCase
from django.contrib.auth.models import User


# tests for the views in the cart app.
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

    def test_get_cart_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        page = self.client.get("/cart/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_empty_cart(self):
        cart = [1, 2, 3]
        cart.pop()
        page = self.client.get("/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_add_to_cart(self):
        self.client.login(username='TheDoctor3', password='tardis')
        product_id = 1
        quantity = int(22)
        cart = [1, 2, 3]

        if quantity > 0:
            cart[product_id] = quantity

        page = self.client.get("/cart/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        self.assertEqual(quantity, cart[1])
