from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from .forms import reviewCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product

# Create your views here.


@login_required
def add_review(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        add_form = reviewCreationForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, "Review successfully created")
            return redirect(reverse('profile'))
        else:
            messages.warning(request, "Unable to create review at this time!")
    else:
        add_form = reviewCreationForm()

    args = {'add_form': add_form, 'product': product}
    return render(request, 'add_review.html', args)
