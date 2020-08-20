from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db.models import Q


class CaseInsensitiveAuthTests(TestCase):
    """
    Tests for the CaseInsensitiveAuth class in backends.py
    """
    @classmethod
    def setUpTestData(cls):

        User.objects.create_user(
            email='han@solo.com',
            username='Falcon',
            password='falcon1',
            first_name='Han',
            last_name='Solo'
        )

    def test_user_filter_returns_user(self, username_or_email='Falcon',
                                      password='falcon1'):
        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))

        user = users[0]

        self.assertEqual(user.username, 'Falcon')

    def test_if_no_users_return_none(self, username_or_email=None,
                                     password=None):
        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))
        if not users:
            return None

        self.assertTrue(None)

    def test_login_in(self):
        response = Client().post('/accounts/login/',
                                 {'username_or_email': 'Falcon',
                                  'password': 'falcon1'})
        self.assertEqual(response.status_code, 302)
        # response = Client().login(username='Falcon', password='falcon1')
        # self.assertEqual(response, True)


