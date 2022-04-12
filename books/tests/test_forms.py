from django.test import SimpleTestCase

from books.forms import RawBookForm


class TestForms(SimpleTestCase):
    def test_raw_form_valid(self):
        form = RawBookForm(data={'q': 'cos',
                                 'title': 'tytul',
                                 'author': 'Kto',
                                 'isbn': '9782123456803'})
        self.assertTrue(form.is_valid())
