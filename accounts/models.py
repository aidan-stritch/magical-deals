from django.db import models
from django.contrib.auth.models import User

class UserAddon(models.Model):
   
    address_line_one = models.CharField(max_length=254, default='')
    address_line_two = models.CharField(max_length=254, default='')
    address_line_three = models.CharField(max_length=254, default='')
    city = models.CharField(max_length=254, default='')
    country = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=254, default='')
    phone = models.CharField(max_length=254, default='')
    profile_image = models.FileField(upload_to='profile')  

    userAddon_fk  = models.ForeignKey(User, null=True, default="1", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.userAddon_fk