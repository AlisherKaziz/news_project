from rest_framework import generics, filters
from news_admin.models import News
from .serializers import NewsUserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PublishedNewsListView(generics.ListAPIView):
    queryset = News.objects.filter(status='published')
    serializer_class = NewsUserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tags', 'category']
    search_fields = ['title', 'content']
