from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserCreate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=254, default='')
    address_line_two = models.CharField(max_length=254, default='')
    address_line_three = models.CharField(max_length=254, default='')
    city = models.CharField(max_length=254, default='')
    country = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=254, default='')
    phone = models.CharField(max_length=254, default='')
    profile_image = models.FileField(upload_to='profile')

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            UserCreate.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.usercreate.save()
