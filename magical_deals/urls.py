"""magical_deals URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home import urls as urls_home
from products import urls as urls_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from search import urls as urls_search
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^', include(urls_home)),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
