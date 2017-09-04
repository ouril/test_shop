from django.conf.urls import url
from userlogin.views import (
    login, 
    logout, 
    login_form, 
    registration
)   

urlpatterns = [
    url(r'login_form/$', login_form, name='login_form'),
    url(r'login/$', login, name='login'),
    url(r'logout/$', logout, name='logout'),
    url(r'^registration/$', registration, name='registration')
]