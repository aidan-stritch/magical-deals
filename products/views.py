from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import ProductCreationForm


# Create your views here.


@login_required
def all_products(request):
    """A view that displays all of the products"""
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def view_product(request, id):
    """
    A view that returns a single
    Product object based on the product ID and
    render it to the 'view_product.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, id=id)

    return render(request, "view_product.html", {'product': product})


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


def delete_product(request, id):
    """
    A view that deletes a single
    Product object based on the product ID and
    redirects the user to the 'products.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, id=id)
    product.delete()

    messages.success(request, "Product successfully deleted")

    return redirect(reverse('products'))
