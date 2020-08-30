from django.forms import ModelForm
from mainapp.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
