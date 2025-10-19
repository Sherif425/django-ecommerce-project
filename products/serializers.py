from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Handles serialization for Category model"""
    class Meta:
        model = Category
        fields = ['id', 'name']  # only existing fields


class ProductSerializer(serializers.ModelSerializer):
    """Handles serialization for Product model"""
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    owner = serializers.ReadOnlyField(source='owner.email')  # fixed from created_by

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock',
            'category', 'category_id', 'owner',
            'created_at', 'updated_at'
        ]
