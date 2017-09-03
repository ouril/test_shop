from django.contrib import admin

# Register your models here.
from .models import (
    Product, 
    Store,
    Order
)

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Order)