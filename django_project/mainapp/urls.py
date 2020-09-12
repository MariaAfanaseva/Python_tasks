from django.urls import path
from mainapp.views import IndexListView, CreateProduct

app_name = 'mainapp'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('create/', CreateProduct.as_view(), name='create'),
]
