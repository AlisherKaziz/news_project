from django.urls import path
from .views import PublishedNewsListView, PublishedNewsDetailView

urlpatterns = [
    path('news/', PublishedNewsListView.as_view(), name='published-news-list'),
]
