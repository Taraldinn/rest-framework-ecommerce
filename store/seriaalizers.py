from rest_framework import serializers
from decimal import Decimal

from store.models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'inventory', 'price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calaculate_tax')

    def calaculate_tax(self, product: Product):
        return product.price * Decimal(1.1)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']













