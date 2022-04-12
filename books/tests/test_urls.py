from django.test import SimpleTestCase
from django.urls import reverse, resolve

from books.views import list_of_books, add, edit, delete, import_book


class TestUrls(SimpleTestCase):
    def test_urls_list(self):
        url = reverse('list_of_books')
        self.assertEquals(resolve(url).func, list_of_books)

    def test_urls_add(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func, add)

    def test_urls_import(self):
        url = reverse('import_book')
        self.assertEquals(resolve(url).func, import_book)

    def test_urls_edit(self):
        url = reverse('edit', args=[1])
        self.assertEquals(resolve(url).func, edit)

    def test_urls_delete(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func, delete)
