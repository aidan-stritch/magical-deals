from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import UserCreate
from .forms import UserLoginForm
from django.contrib.auth.models import User


# tests for the views in the accounts app.
class ViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='whosthedoctor@gallifrey.com',
            username='TheDoctor',
            password='tardis',
            first_name='Doctor',
            last_name='Who'
        )

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_register_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "sign-up.html")

    def test_get_profile_page(self):
        user = User.objects.get(username='TheDoctor')

        page = self.client.get('/accounts/profile/', {user})
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
