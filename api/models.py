from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='create')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='update')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    serial_num = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=200)
    manufacturing_date = models.DateField(auto_now=True)
    stock = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'product'


class Category(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
