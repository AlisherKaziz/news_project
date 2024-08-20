from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import News, Category, Tag
from .serializers import NewsAdminSerializer, CategorySerializer, TagSerializer
from .permissions import IsAdminUser
from .filters import NewsFilter

class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsAdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filterset_class = NewsFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsAdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
