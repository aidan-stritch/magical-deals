from django.conf.urls import url
from .views import all_products, add_product, view_product
from .views import delete_product, edit_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^add_product/$', add_product, name='add_product'),
    url(r'^(?P<id>\d+)/edit/$', edit_product, name='edit_product'),
    url(r'^(?P<id>\d+)/$', view_product, name='view_product'),
    url(r'^(?P<id>\d+)/delete/$', delete_product, name='delete_product'),
]
