from django.test import TestCase
from .models import UserCreate
from django.contrib.auth.models import User

# Create your tests here.


class AccountModelTests(TestCase):
    """
    Tests for the UserCreate model
    """
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='whosthedoctor@gallifrey.com',
            username='TheDoctor',
            password='tardis',
            first_name='Doctor',
            last_name='Who'
        )

    def test_str(self):

        test_address_1 = UserCreate(address_line_one='This is an address')
        test_address_2 = UserCreate(address_line_two='This is an address')
        test_address_3 = UserCreate(address_line_three='This is an address')
        test_profile_image = UserCreate(profile_image='testimage.jpg')
        test_city = UserCreate(city='Dublin')
        test_country = UserCreate(country='Ireland')
        test_postcode = UserCreate(postcode='D085523')
        test_phone = UserCreate(phone='555-8859')

        self.assertEqual(str(test_address_1.address_line_one),
                         'This is an address')
        self.assertEqual(str(test_address_2.address_line_two),
                         'This is an address')
        self.assertEqual(str(test_address_3.address_line_three),
                         'This is an address')
        self.assertEqual(str(test_profile_image.profile_image),
                         'testimage.jpg')
        self.assertEqual(str(test_city.city), 'Dublin')
        self.assertEqual(str(test_country.country), 'Ireland')
        self.assertEqual(str(test_postcode.postcode), 'D085523')
        self.assertEqual(str(test_phone.phone), '555-8859')

    def test_done_defaults_to_True(self):
        user = User.objects.create_user(
            email='whosthemaster@gallifrey.com',
            username='TheMaster',
            password='tardis',
            first_name='The',
            last_name='Master'
        )

        user.save()
        self.assertTrue(user.save)
