from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from .forms import reviewCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review

# Create your views here.


@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        add_form = reviewCreationForm(request.POST)
        if add_form.is_valid():
            review = add_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()

            messages.success(request, "Review successfully created")
            return redirect(reverse('profile'))
        else:
            messages.warning(request, "Unable to create review at this time!")
    else:
        add_form = reviewCreationForm()

    args = {'product': product, 'add_form': add_form}
    return render(request, 'add_review.html', args)


@login_required
def edit_review(request, id):
    """A view that allows a user to edit a review"""
    review = get_object_or_404(Review, id=id)

    if request.method == 'POST':
        edit_form = reviewCreationForm(request.POST, instance=review)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(
                request, "Review has successfully been updated!")
            return redirect(reverse('profile'))
        else:
            messages.error(
                request, "Unable to update. Please rectify the problems below")
    else:
        edit_form = reviewCreationForm(instance=review)

    args = {
        'edit_form': edit_form,
        "review": review
    }
    return render(request, 'edit_review.html', args)


@login_required
def delete_review(request, id):
    """
    A view that deletes a single
    review object based on the review ID and
    redirects the user to the 'profile.html' template.
    Or return a 404 error if the review is
    not found
    """
    review = get_object_or_404(Review, id=id)
    review.delete()
    messages.success(request, "Review successfully deleted")
    return redirect(reverse('profile'))
