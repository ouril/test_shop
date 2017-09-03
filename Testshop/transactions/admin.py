from django.contrib import admin

# Register your models here.
from .models import UserBalance, UserBalanceChange

admin.site.register(UserBalance)
admin.site.register(UserBalanceChange)