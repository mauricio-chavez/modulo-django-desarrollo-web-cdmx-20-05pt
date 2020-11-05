"""Products app serializers"""

from rest_framework import serializers

from .models import Product

# Hyperlinked serializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Product hyperlinked serializer"""
    class Meta:
        """Meta data of serializer"""
        model = Product
        fields = ['url', 'name', 'price', 'rating']

# Model serializer

# class ProductSerializer(serializers.ModelSerializer):
#     """Product model serializer"""
#     class Meta:
#         """Meta data of serializer"""
#         model = Product
#         fields = ['id', 'name', 'price', 'rating']

# Basic serializer

# class ProductSerializer(serializers.Serializer):
#     """My product serializer"""
#     id = serializers.IntegerField(label='ID', read_only=True)
#     name = serializers.CharField()
#     price = serializers.DecimalField(max_digits=9, decimal_places=2)
#     rating = serializers.IntegerField()

#     def create(self, validated_data):
#         """Saves a product"""
#         return Product.objects.create(**validated_data)

#     def update(self, product, validated_data):
#         """Updates a product"""
#         product.name = validated_data.get('name', product.name)
#         product.price = validated_data.get('price', product.price)
#         product.rating = validated_data.get('rating', product.rating)
#         product.save()

#         return product
