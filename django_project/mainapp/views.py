from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from mainapp.models import Product
from mainapp.forms import ProductForm


class IndexListView(ListView):
    template_name = 'mainapp/index.html'
    model = Product
    context_object_name = 'product_list'


class CreateProduct(View):
    new_product = 'mainapp/new_product.html'
    products_table = 'mainapp/products_table.html'
    form = ProductForm
    response = {'result': ''}

    def get(self, request):
        self.response['result'] = render_to_string(self.new_product,
                                                   {'form': ProductForm()},
                                                   request=request)
        return JsonResponse(self.response)

    def post(self, request):
        add_product_form = self.form(request.POST)
        if add_product_form.is_valid():
            add_product_form.save()
            self.response['form_is_valid'] = True
            self.response['result'] = render_to_string(self.products_table,
                                                       {'product_list': Product.objects.all()},
                                                       request=request)
        else:
            print(add_product_form.errors)
            self.response['form_is_valid'] = False
            self.response['result'] = render_to_string(self.new_product,
                                                       {'form': add_product_form},
                                                       request=request)
        return JsonResponse(self.response)

