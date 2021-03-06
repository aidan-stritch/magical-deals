from django.shortcuts import render
from products.models import Product
from checkout.models import Order, OrderLineItem


# Create your views here.
def index(request):
    """Displays the index page."""
    products = Product.objects.all()
    orders = Order.objects.all()
    """When running on Gitpod (using Sqlite3 DB) remove
    the 'distinct' below. This feature does not work on
    Sqlite3, but works perfectly on postgres."""
    items = OrderLineItem.objects.order_by('product_id').distinct('product_id')
    args = {"products": products, "orders": orders, "items": items}
    return render(request, "index.html", args)


def about(request):
    """Displays the about us page."""
    return render(request, "about.html")
