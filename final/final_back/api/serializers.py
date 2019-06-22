from rest_framework import serializers
from .models import Product, UserProduct
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, allow_null= True)
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.name)
        instance.quantity = validated_data.get('quantity', instance.name)
        instance.save()
        return instance


class UserProductSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null= True)
    user = UserSerializer(read_only=True)
    product = ProductSerializer()
    count = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ('id', 'user', 'product', 'count')


    def create(self, validated_data):
        products = validated_data.pop('product')
        user_products = UserProduct.objects.create(**validated_data)
        for product in products:
            Product.objects.create(user_products=user_products, **product)

        return user_products