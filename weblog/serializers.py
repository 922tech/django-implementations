from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()

        return instance


class BlogFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogFile
        fields = '__all__'

    def create(self, validated_data):
        return BlogFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.files = validated_data['files']
        instance.url = validated_data['url']
        instance.save()
        return instance


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'

    def create(self, validated_data):
        return BlogImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data['image']
        instance.url = validated_data['url']
        instance.save()

        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.category = validated_data['category']
        # instance.slug = validated_data['slug']
        instance.writer = validated_data['writer']
        instance.content = validated_data['content']
        instance.comment = validated_data['comment']
        # instance.tags = validated_data['tags']

        if 'thumbnail' in validated_data.keys():
            instance.thumbnail = validated_data['thumbnail']
        instance.save()

        return instance

