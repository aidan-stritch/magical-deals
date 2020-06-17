from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    rating = models.IntegerField()

    def __str__(self):
        return self.product_name
