from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"





