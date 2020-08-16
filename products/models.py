from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=254, default='',
                                    help_text='Please choose a catchy name')
    description = models.TextField(help_text='Add an appealing description')
    price = models.DecimalField(max_digits=100, decimal_places=2,
                                help_text='Minimum price €1.00',
                                validators=[MinValueValidator(0.50)])
    image = models.ImageField(upload_to='images',
                              help_text='Mandatory')
    rating = models.IntegerField(default=0,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(10)],
                                 help_text='Min 0, Max 10')

    def __str__(self):
        return self.product_name
