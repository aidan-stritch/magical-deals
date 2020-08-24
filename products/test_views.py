from django.test import TestCase
from django.contrib.auth.models import User
from products.forms import ProductCreationForm
from products.models import Product


# tests for the views in the products app.
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

    def test_get_all_products_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        products = []

        page = self.client.get("/products/", {"products": products})

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_add_product_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        test_add_form = ProductCreationForm()

        page = self.client.get("/products/add_product/",
                               {"test_add_form": test_add_form})

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_product.html")

    def test_get_view_product_page(self):
        test_product = Product(
                    id="1",
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )

        product = test_product
        reviews = []
        orders = []

        args = {"reviews": reviews, "product": product, "orders": orders}

        page = self.client.get("/products/view_product/", args)

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_product.html")

    def test_get_edit_product_page(self):
        test_product = Product(
                    id="1",
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )

        test_edit_form = ProductCreationForm(instance=test_product)
        args = {"test_product": test_product, "test_edit_form": test_edit_form}

        page = self.client.get("/products/edit_product/", args)

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_product.html")

    def test_delete_product(self):
        self.client.login(username='TheDoctor3', password='tardis')
        products = []
        test_product = Product(
                    id="1",
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )
        test_product.delete()

        page = self.client.get("/products/", {"products": products})

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
