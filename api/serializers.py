from django.contrib.auth.models import User
from rest_framework import serializers
from .models import JournalPost, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class JournalPostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = JournalPost
        fields = ['id','author', 'title', 'content', 'category', 'date', 'slug']
        extra_kwargs = {"author": {"read_only": True}}
