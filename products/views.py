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


@login_required
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


@login_required
def delete_product(request, id):
    """
    A view that deletes a single
    Product object based on the product ID and
    redirects the user to the 'products.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    """ ask tutor on this one. here we are pulling in the product
    id and the cart. i am then trying to check if the product is
    in the cart.. if so pop it out before moving on.. if not
    just delete the product.. """
    if cart[id] == product:
        cart.pop(id)

    cart.pop(id)
    product.delete()

    messages.success(request, "Product successfully deleted")

    return redirect(reverse('products'))


@login_required
def edit_product(request, id):
    """A view that allows a user to edit a products details"""
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':

        edit_form = ProductCreationForm(
            request.POST, request.FILES, instance=product)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(
                request, "Product has successfully been updated!")
            return redirect(view_product, product.id)
        else:
            messages.error(
                request, "Unable to update. Please rectify the problems below")
    else:
        edit_form = ProductCreationForm(instance=product)

    args = {
        'edit_form': edit_form,
        "product": product
    }
    return render(request, 'edit_product.html', args)



