from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    """ A model to handle a customers delivery address
    when they checkout of the store from the cart"""
    user = models.ForeignKey(User)
    phone_Number = models.CharField(max_length=20, blank=False)
    address_Line_One = models.CharField(max_length=40, blank=False)
    address_Line_Two = models.CharField(max_length=40, blank=False)
    address_Line_Three = models.CharField(max_length=40, blank=False)
    town_or_City = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.user)


class OrderLineItem(models.Model):
    """ A model to handle a customers order
    when they checkout of the store from the cart"""
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity,
                                      self.product.product_name,
                                      self.product.price, self.order)
