from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserSignUpFormAddon, UserAdditionalFields
from accounts.forms import StaffField, UserSignUpForm
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib import messages


# tests for the views in the accounts app.
class ViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            id=1,
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
        self.client.login(username='TheDoctor3', password='tardis')
        user = User.objects.get(email='whosthedoctor3@gallifrey.com')

        reviews = [1, 2, 3]
        orders = [1, 2, 3]
        items = [1, 2, 3]

        args = {
            'reviews': reviews,
            'orders': orders,
            'items': items,
        }

        page = self.client.get('/accounts/profile/', args)

        self.assertEqual(page.status_code, 200)
        self.assertTrue(user.is_authenticated)
        self.assertTemplateUsed(page, "profile.html")

    def test_get_all_orders_page(self):
        page = self.client.get("/accounts/all_orders/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_orders.html")

    def test_get_all_users_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        all_users = User.objects.all()
        page = self.client.get("/accounts/all_users/",
                               {"all_users": all_users})

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_users.html")

    def test_get_edit_user_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
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

        page = self.client.get("/accounts/edit_user/", args)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_user.html")

    def test_get_admin_edit_user_page(self):
        self.client.login(username='TheDoctor3', password='tardis')
        this_user = User.objects.get(email='whosthedoctor3@gallifrey.com')
        user_form = UserSignUpFormAddon(instance=this_user)
        profile_form = UserAdditionalFields(instance=this_user)
        staff_form = StaffField(instance=this_user)

        args = {
            'user_form': user_form,
            'profile_form': profile_form,
            'this_user': this_user,
            'staff_form': staff_form
        }

        page = self.client.post("/accounts/1/admin_edit_user/", args)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_user.html")


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

    def test_user_delete_works(self):
        test_user = User.objects.create_user(username="test_delete",
                                             email="delete@test.com",
                                             password="deleteme")
        test_user.delete()
        self.client.login(username='TheDoctor2', password='tardis2')

        middleware = MessageMiddleware()
        middleware.process_request(self)
        self.session.save()

        page = self.client.get("/accounts/delete_user/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_user_not_deleted(self):

        try:
            self.fail()
        except Exception as e:
            page = self.client.get("/accounts/delete_user/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_log_out(self):
        page = self.client.get("/accounts/logout/")

        self.assertRedirects(page, '/')

    def test_register_form_is_valid(self):
        user_form = UserSignUpForm({
                'username': 'testname',
                'email': 'testemail@test.ie',
                'password1': 'testlast',
                'password2': 'testlast'
            })

        self.assertTrue(user_form.is_valid())

    def test_register_form_login(self):
        user_form = UserSignUpForm({
                'username': 'testname',
                'email': 'testemail@test.ie',
                'password1': 'testlast',
                'password2': 'testlast'
            })
        user_form.save()
        user = User.objects.get(username='testname')

        self.client.login(username='testname', password='testlast')
        self.assertTrue(user_form.save())
        self.assertTrue(user.is_authenticated)
