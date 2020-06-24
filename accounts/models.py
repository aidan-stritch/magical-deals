from django.db import models
from django.conf import settings

class userAddon(models.Model):
   
    address_line_one = models.CharField(max_length=254, default='')
    address_line_two = models.CharField(max_length=254, default='')
    address_line_three = models.CharField(max_length=254, default='')
    city = models.CharField(max_length=254, default='')
    country = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=254, default='')
    phone = models.CharField(max_length=254, default='')
    profile_image = models.FileField(upload_to='profile')  

    userAddon_fk = models.ForeignKey(settings.AUTH_USER_MODEL) 

    def __str__(self):
        return self.userAddon_fk