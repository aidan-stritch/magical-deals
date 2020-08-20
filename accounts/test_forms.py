from django.test import TestCase
from .forms import UserSignUpFormAddon, UserAdditionalFields
from .forms import UserLoginForm, UserSignUpForm
from django.core.exceptions import ValidationError


# tests for the forms in the accounts app.


class UserLoginFormTests(TestCase):
    """
    Tests for the UserCreate UserLoginForm form
    """
    def test_cannot_login_with_invalid_form(self):
        login_form = UserLoginForm({'username_or_email': 'formtest'})
        self.assertFalse(login_form.is_valid())


class UserSignUpFormTests(TestCase):
    """
    Tests for the UserCreate UserSignUpForm form
    """

    def test_cannot_signup_with_invalid_form(self):
        signup_form = UserSignUpForm({'password1': ''})
        self.assertFalse(signup_form.is_valid())
        self.assertEqual(signup_form.errors['password1'],
                         [u'Please enter a valid password'])

    def test_password_validation_not_empty(self):
        password1 = "test"
        password2 = ""

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        self.assertRaises(ValidationError)

    def test_password_validation_match(self):
        password1 = "test"
        password2 = "test2"

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        self.assertRaises(ValidationError)


class UserSignUpFormAddonTests(TestCase):
    """
    Tests for the UserCreate UserSignUpFormAddon form
    """
    def test_can_create_user_with_just_a_name(self):
        user_form = UserSignUpFormAddon({'first_name': 'Aidan'})
        self.assertTrue(user_form.is_valid())


class UserAdditionalFieldsTests(TestCase):
    """
    Tests for the UserCreate UserAdditionalFields form
    """
    def test_cannot_create_user_with_just_a_city(self):
        user_form = UserAdditionalFields({'city': 'Dublin'})
        self.assertFalse(user_form.is_valid())

    def test_correct_message_for_missing_profile_image(self):
        user_form = UserAdditionalFields({'profile_image': ''})
        self.assertFalse(user_form.is_valid())
        self.assertEqual(user_form.errors
                         ['profile_Image'], [u'This field is required.'])
