from django_filters import rest_framework as filters
from .models import News

class NewsFilter(filters.FilterSet):
    class Meta:
        model = News
        fields = {
            'title': ['icontains'],
            'content': ['icontains'],
            'category': ['exact'],
            'tags': ['exact'],
            'status': ['exact'],
        }
