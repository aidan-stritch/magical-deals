from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ to avoid overwriting static files on S3 when creating new products"""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ handles media files"""
    location = settings.MEDIAFILES_LOCATION
