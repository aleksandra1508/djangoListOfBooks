from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    date_of_publication = models.CharField(blank=False, max_length=50)
    isbn = ISBNField(blank=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    image_link = models.URLField(max_length=500, blank=True)
    language = models.CharField(max_length=2, blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
