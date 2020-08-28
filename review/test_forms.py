from django.test import TestCase
from .forms import reviewCreationForm


# tests for the form in the review app.
class reviewCreationFormTests(TestCase):
    """Tests for the UserCreate reviewCreationForm form."""
    def test_form_is_valid_with_all_fields(self):
        review_form = reviewCreationForm({'description': 'this is a test',
                                         'rating': '8'})
        self.assertTrue(review_form.is_valid())

    def test_form_is_not_valid_with_empty_fields(self):
        review_form = reviewCreationForm({'description': '',
                                         'rating': ''})
        self.assertFalse(review_form.is_valid())

    def test_form_is_not_valid_with_rating_more_then_ten(self):
        review_form = reviewCreationForm({'description': 'this is a test',
                                         'rating': '11'})
        self.assertFalse(review_form.is_valid())
