from django.conf.urls import url
from .views import product_search

urlpatterns = [
    url(r'^$', product_search, name='search')
]
