from django.conf.urls import url
from .views import add_review

urlpatterns = [
    url(r'^(?P<pk>\d+)/add_review/$', add_review, name='add_review'),
]
