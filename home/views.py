from django.shortcuts import render
from products.models import Product


# Create your views here.


def index(request):
    """displays the index page"""
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def about(request):
    """displays the about us page"""

    return render(request, "about.html")
