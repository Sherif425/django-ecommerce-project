from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Handles serialization for Category model"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    """Handles serialization for Product model"""
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    created_by = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'in_stock',
            'category', 'category_id', 'created_by',
            'created_at', 'updated_at'
        ]
