from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import UserCreate

# tests for the views in the accounts app.


class ViewTests(TestCase):
    def test_get_register_page(self):
        page = self.client.get("/register")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "sign-up.html")
