import django_filters
from django_filters import CharFilter, DateFilter

from .models import Book


class BookFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',
                       label='Title: ')
    author = CharFilter(field_name='author', lookup_expr='icontains', label='Author:')
    language = CharFilter(field_name='language', lookup_expr='icontains',
                          label='Language: ')
    start_date = DateFilter(field_name="date_of_publication", lookup_expr='gte')
    end_date = DateFilter(field_name="date_of_publication", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author', 'language']
