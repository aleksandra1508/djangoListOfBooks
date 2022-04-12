from django.test import TestCase
from django.urls import reverse

from books.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(
            title='Diuna',
            author='Frank Herbert',
            date_of_publication='1965',
            isbn='9788381881388',
            number_of_pages=783,
            image_link='https://image.ceneostatic.pl/data/products/528076/i-diuna.jpg',
            language='en'
        )

    def test_list_of_books(self):
        url = reverse('list_of_books')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_add(self):
        url = reverse('add')
        response = self.client.post(
            url, {
                'title': 'Diuna',
                'author': 'Frank Herbert',
                'date_of_publication': '1965'
            }, follow=True
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')
        self.assertTrue(Book.objects.filter(title='Diuna'))

    def test_add_book_search(self):
        url = reverse('add')
        response = self.client.get(
            url, {
                'q': 'Hobbit',
            }, follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/add.html')

    def test_import_book(self):
        url = reverse('import_book')
        response = self.client.post(
            url, {
                'title': 'Hobbit',
                'author': 'Tolkien',
                'date_of_publication': '1960',
                'isbn': '1231231232',
                'number_of_pages': '123',
                'image_link': 'http://books.google.com/books/content?id=DqLPAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api',
                'language': 'en'
            }, follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_edit_book(self):
        book_id = Book.objects.get(title='Diuna').id
        url = reverse('edit', args=[book_id])
        response = self.client.post(
            url, {
                'title': 'test',
                'author': 'test',
                'date_of_publication': '2020-10-10'
            }, follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')
        self.assertEquals(Book.objects.filter(title='test').count(), 1)

    def test_delete(self):
        book_id = Book.objects.get(title='Diuna').id
        url = reverse('delete', args=[book_id])

        response = self.client.post(
            url, follow=True
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')
        self.assertEquals(Book.objects.all().count(), 0)

