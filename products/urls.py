from django.conf.urls import url
from .views import all_products, add_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^add_product/$', add_product, name='add_product'),
]
