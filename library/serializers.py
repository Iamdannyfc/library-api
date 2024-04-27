
from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    # Serializer for Category model
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']  # Fields to include in the serialized representation

class BookSerializer(serializers.ModelSerializer):
    # Serializer for Book model
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'no_of_pages', 'description', 'category', 'created_at', 'updated_at']  # Fields to include in the serialized representation

