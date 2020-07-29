from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from .forms import reviewCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product

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
