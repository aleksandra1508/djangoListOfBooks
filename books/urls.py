from django.urls import path
from books.views import list_of_books, add, edit, delete, import_book


urlpatterns = [
    path('', list_of_books, name='list_of_books'),
    path('add/', add, name='add'),
    path('import/', import_book, name='import_book'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
]
