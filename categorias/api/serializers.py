from rest_framework import serializers
from categorias.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title', 'slug', 'published']