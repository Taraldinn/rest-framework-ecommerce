from rest_framework import serializers
from decimal import Decimal

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'price', 'price_with_tax', 'inventory', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calaculate_tax')

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail',
    # )

    def calaculate_tax(self, product: Product):
        return product.price * Decimal(1.1)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return serializers.ValidationError('Password do not match')
        return data

    def create(self, validate_data):
        product = Product(**validate_data)
        product.other = 1
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.unit_price = validated_data.get('unit_price', )
        instance.save()
        return instance
