from django.conf.urls import url
from .views import ProductDetailView, ProductListView


urlpatterns = [
    url(r'products$', ProductListView.as_view(), name='list'),
    url(r'products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail')
]