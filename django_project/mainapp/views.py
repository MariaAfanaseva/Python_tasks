from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from mainapp.models import Product


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Product
    context_object_name = 'product_list'


class CreateProduct(CreateView):
    template_name = 'mainapp/new_product.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('main:index')
