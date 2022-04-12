from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer


class RestAPIView(viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = {
        'title': ['icontains'],
        'authors': ['icontains'],
        'language': ['icontains'],
        'published_date': ['gte', 'lte']
    }
    search_fields = ['title', 'authors', 'language']
