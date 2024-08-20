from rest_framework import serializers
from news_admin.models import News

class NewsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'content', 'slug', 'published_at', 'tags', 'category']
