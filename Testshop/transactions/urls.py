from django.conf.urls import url
from .views import buy

urlpatterns = [
    url(r'buy/(?P<pk>\d+)/$', buy, name='buy'),
]