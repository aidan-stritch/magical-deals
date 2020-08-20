from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserSignUpFormAddon, UserAdditionalFields
from accounts.forms import StaffField


# tests for the views in the accounts app.
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

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_sign_up_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "sign-up.html")

    def test_get_profile_page(self):
        user = User.objects.get(username='TheDoctor3')
        reviews = []
        orders = []
        items = []

        args = {
            'user': user,
            'reviews': reviews,
            'orders': orders,
            'items': items,
        }

        page = self.client.post('/accounts/profile', args)

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "profile.html")
        

    def test_get_all_orders_page(self):
        page = self.client.get("/accounts/all_orders/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_orders.html")

    def test_get_all_users_page(self):
        page = self.client.get("/accounts/all_users/")

        all_users = User.objects.all()

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_users.html",
                                {"all_users": all_users})

    def test_get_edit_user_page(self):
        this_user = User.objects.get(email='whosthedoctor3@gallifrey.com')
        user_form = UserSignUpFormAddon(instance=this_user)
        profile_form = UserAdditionalFields(instance=this_user)
        staff_form = StaffField(instance=this_user)
        args = {
            'user_form': user_form,
            'profile_form': profile_form,
            'staff_form': staff_form,
            'this_user': this_user
        }

        page = self.client.get("/accounts/edit_user/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_user.html", args)


# tests for the views in the accounts app.
class ViewFunctionalityTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
                email='whosthedoctor2@gallifrey.com',
                username='TheDoctor2',
                password='tardis2',
                first_name='Doctor2',
                last_name='Who2'
            )

    def test_login_works_with_valid_fields(self):

        user = User.objects.get(username='TheDoctor2')

        page = self.client.post('/accounts/login', {
            'username': 'TheDoctor2',
            'password': 'tardis',
        }, follow=True)

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)

        
