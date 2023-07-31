from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return super().create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.category = validated_data['category']
        instance.image = validated_data['image']
        instance.brand = validated_data['brand']
        instance.price = validated_data['price']
        instance.short_description = validated_data['short_description']
        instance.description = validated_data['description']
        # instance.slug = validated_data['slug']
        instance.is_active = validated_data['is_active']
        instance.is_delete = validated_data['is_delete']
        instance.tags = validated_data['tags']

        return super().update(instance, validated_data)

    # def create(self, instance, validated_data):

    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'



