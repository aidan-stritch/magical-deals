from django.conf.urls import url
from .views import add_review, edit_review, delete_review, all_reviews

urlpatterns = [
    url(r'^(?P<pk>\d+)/add_review/$', add_review, name='add_review'),
    url(r'^(?P<pk>\d+)/edit_review/$', edit_review, name='edit_review'),
    url(r'^(?P<id>\d+)/delete_review/$', delete_review, name='delete_review'),
    url(r'^all_reviews/$', all_reviews, name="all_reviews"),
]
