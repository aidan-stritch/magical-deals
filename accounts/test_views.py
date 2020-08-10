from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import UserCreate
from .forms import UserLoginForm


# tests for the views in the accounts app.
class ViewTests(TestCase):
    def test_get_login_page(self):
        page = self.client.get("/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html")

    def test_get_register_page(self):
        page = self.client.get("/register")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "sign-up.html")

    def test_get_profile_page(self):
        page = self.client.get("/profile")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
