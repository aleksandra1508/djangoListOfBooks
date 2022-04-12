from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer


class RestAPIView(viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'title': ['icontains'],
        'author': ['icontains'],
        'language': ['icontains'],
        'date_of_publication': ['gte', 'lte']
    }
    search_fields = ['title', 'author', 'language']
