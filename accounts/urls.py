from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, logout
from .views import login, edit_user, delete_user, all_orders

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^edit_user/$', edit_user, name='edit_user'),
    url(r'^delete_user/$', delete_user, name='delete_user'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^all_orders/$', all_orders, name='all_orders'),
]
