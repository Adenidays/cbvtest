from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from shop.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "show_products.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug_param"


class AddProductView(CreateView):
    model = Product
    form_class = modelform_factory(Product, fields="__all__")
    template_name = "add_product.html"
    success_url = reverse_lazy("show_products")


# views.py

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = ['title', 'price']
    slug_field = 'slug'
    slug_url_kwarg = 'param'
    success_url = reverse_lazy('show_products')


class ProductDeleteView(DeleteView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'params'
    template_name = 'delete_product.html'
    success_url = reverse_lazy('show_products')
