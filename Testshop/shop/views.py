from django.shortcuts import render
from django.contrib import auth

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    template_name = "list.html"
    model = Product
    queryset = Product.objects.order_by("created").reverse()

class ProductDetailView(DetailView):
    template_name = "detail.html"
    model = Product


