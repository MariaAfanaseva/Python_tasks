from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='product name', unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0,
                                verbose_name='product price')

    def __str__(self):
        return f'{self.name}'
