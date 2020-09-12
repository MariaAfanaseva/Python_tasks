from django.contrib import admin
from mainapp.models import (
    Product
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = 'name',
