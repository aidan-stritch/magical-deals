from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, null=False)
    user = models.ForeignKey(User)

    description = models.TextField(help_text='Add an appealing description')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Min 0, Max 10')

    def __str__(self):
        return "{0} {1} @ {2}".format(self.description,
                                      self.product.product_name,
                                      self.rating,
                                      self.user.username)
