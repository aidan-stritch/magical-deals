from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserCreate(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    add_Line_One = models.CharField(max_length=254, default='',
                                    help_text='e.g. Apt Number')
    add_Line_Two = models.CharField(max_length=254, default='',
                                    help_text='e.g. Street')
    add_Line_Three = models.CharField(max_length=254, default='')
    city = models.CharField(max_length=254, default='')
    country = models.CharField(max_length=254, default='')
    postcode = models.CharField(max_length=254, default='')
    phone = models.CharField(max_length=254, default='',
                             help_text='e.g. +353 (0) 555 2258')
    profile_Image = models.FileField(upload_to='profile',
                                     help_text='Please use a clear image')
    staff = models.BooleanField(default=False,
                                help_text='Please indicate whether this user is staff or not')

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            UserCreate.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.usercreate.save()
