from rest_framework import serializers
from .models import News, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class NewsAdminSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = News
        fields = '__all__'
