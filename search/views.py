from django.shortcuts import render
from products.models import Product
from django.contrib import messages

# Create your views here.


def product_search(request):
    """A function that uses built in django functionility
    to return a list of products based on a search."""

    products = Product.objects.filter(product_name__icontains=request.GET['q'])

    if products:
        return render(request, "products.html", {"products": products})
    else:
        messages.error(request, "No results for your query")
        return render(request, "products.html")
