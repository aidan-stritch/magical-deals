from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    address_line_one = forms.CharField(label='Address Line 1')
    address_line_two = forms.CharField(label='Address Line 2')
    address_line_three = forms.CharField(label='Address Line 3')
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')
    postcode = forms.CharField(label='Postcode')
    phone = forms.CharField(label='Phone')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name',
                  'last_name', 'address_line_one', 'address_line_two',
                  'address_line_three', 'postcode', 'city', 'country',
                  'phone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
