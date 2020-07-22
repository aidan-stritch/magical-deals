from django.db import models
from products.models import Product

# Create your models here.


class Order(models.Model):
    """ A model to handle a customers order
    when they checkout of the store from the cart"""

    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    add_line_one = models.CharField(max_length=40, blank=False)
    add_line_two = models.CharField(max_length=40, blank=False)
    add_line_three = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    oder = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity,
                                      self.product.name, self.product.price)
