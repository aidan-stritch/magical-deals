from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserSignUpForm, UserSignUpFormAddon
from django.contrib.auth.decorators import login_required
from .models import UserAddon

# Create your views here.


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                user_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    userDetails = get_object_or_404(UserAddon, userAddon_fk=request.user)
    print(userDetails)
    return render(request, 'profile.html', userDetails)


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        user_form_addon = UserSignUpFormAddon(request.POST, request.FILES)

        if user_form.is_valid() and user_form_addon.is_valid():
            user_form.save()
            user_form_addon.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserSignUpForm()
        user_form_addon = UserSignUpFormAddon()

    args = {'user_form_addon': user_form_addon, 'user_form': user_form}
    return render(request, 'sign-up.html', args)
