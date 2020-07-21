from django.shortcuts import render
from products.models import Product

# Create your views here.


def product_search(request):
    """ a function that uses built in django functionility
    to return a list of products based on a search """

    products = Product.objects.filter(product_name__icontains=request.GET['q'])

    return render(request, "products.html", {"products": products})
