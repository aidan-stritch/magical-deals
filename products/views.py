from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import ProductCreationForm


# Create your views here.


@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def add_product(request):
    """A view that manages the add product form"""
    if request.method == 'POST':
        add_form = ProductCreationForm(request.POST, request.FILES)
        if add_form.is_valid():
            print(f"add_form is valid and it is {add_form}")
            add_form.save()

            messages.success(request, "Product successfully created")
            return redirect(reverse('products'))

        else:
            messages.warning(request, "Unable to create product at this time!")
    else:
        add_form = ProductCreationForm()

    args = {'add_form': add_form}
    return render(request, 'add_product.html', args)
