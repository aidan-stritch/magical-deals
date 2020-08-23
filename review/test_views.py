from django.test import TestCase
from django.contrib.auth.models import User
from review.forms import reviewCreationForm
from products.models import Product
from .models import Review



# tests for the views in the review app.
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

    def test_get_add_review_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')

        test_product = Product(
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )
        add_form = reviewCreationForm()

        args = {'test_product': test_product, 'add_form': add_form}

        page = self.client.get('/review/add_review/', args)

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "add_review.html")

    def test_delete_review(self):
        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')
        test_product = Product(
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )

        review = Review(
                    id='1',
                    product=test_product,
                    user=user,
                    description='this is a test',
                    rating='8'
                )

        review.delete()

        page = self.client.get('/accounts/profile/')

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "profile.html")

    def test_view_all_reviews_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')
        test_product = Product(
                    product_name='testproduct',
                    description='this is a test description',
                    price='13.99',
                    image='test.jpg',
                    rating='8'
                )
        review = Review(
                    id='1',
                    product=test_product,
                    user=user,
                    description='this is a test',
                    rating='8'
                )

        args = {"review": review} 

        page = self.client.get('/review/all_reviews/', args)

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "all_reviews.html")
