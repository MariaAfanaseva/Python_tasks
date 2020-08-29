from django.views.generic import ListView
from mainapp.models import Product


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Product
    context_object_name = 'product_list'
