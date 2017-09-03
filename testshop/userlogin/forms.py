from django import forms
from django.contrib.auth.models import User

class RegForm(UserCreationForm):                                                                
    class Meta:
        model = User
        fields = ('username','email')