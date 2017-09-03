from django.conf.urls import url
from userlogin.views import login, logout, loged

urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'loged/$', loged, name='loged'),
    url(r'logout/$', logout, name='logout'),
]