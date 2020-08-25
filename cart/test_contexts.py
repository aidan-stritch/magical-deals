from django.test import TestCase


class TestCartConfig(TestCase):
    def test_calculation(self):
        total = 100
        quantity = 2
        price = 10
        product_count = 5

        total += quantity * price
        product_count += quantity

        self.assertEqual(total, 120)
