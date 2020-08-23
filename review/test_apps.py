from django.apps import apps
from django.test import TestCase
from .apps import ReviewConfig


class TestReviewConfig(TestCase):
    def test_app(self):
        self.assertEqual("review", ReviewConfig.name)
        self.assertEqual("review", apps.get_app_config("review").name)
