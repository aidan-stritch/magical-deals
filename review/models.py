from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Product

# Create your models here.


class Review(models.Model):
    product = models.ForeignKey(Product, null=False)
    description = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return "{0} {1} @ {2}".format(self.description,
                                      self.product.product_name, self.rating)
