from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookForm, RawBookForm
from books.models import Book
from .filters import BookFilter
from books.import_book_API import imported_books, json_to_list


def list_of_books(request, *args, **kwargs):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs
    context = {'book_filter': book_filter,
               'books': books}
    return render(request, "books/books.html", context)


def add(request):
    form = BookForm()
    raw_book_form = RawBookForm()
    import_books = {}
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully added')
            return redirect('list_of_books')

    if request.method == 'GET' and 'search_book' in request.GET:
        raw_book_form = RawBookForm(request.GET)
        if raw_book_form.is_valid():
            queries = raw_book_form.cleaned_data
            if not(queries['q'] == "" and queries['title']
                   == "" and queries['author'] == "" and queries['isbn'] == ""):
                search = imported_books(queries)
                import_books = json_to_list(search)
    context = {'form': form, 'raw_book_form': raw_book_form,
               'import_books': import_books}
    return render(request, 'books/add.html', context)


def import_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            date_of_publication=request.POST.get('date_of_publication'),
            isbn=request.POST.get('isbn'),
            number_of_pages=request.POST.get('number_of_pages'),
            image_link=request.POST.get('image_link'),
            language=request.POST.get('language')
        )
        messages.success(request, 'Book successfully imported')
        return redirect('list_of_books')


def edit(request, pk):
    book = get_object_or_404(Book, id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully updated')
            return redirect('list_of_books')
    context = {'form': form}
    return render(request, 'books/add.html', context)


def delete(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        book.delete()
        messages.warning(request, 'Book successfully deleted')
        return redirect('list_of_books')
    context = {'book': book}
    return render(request, 'books/delete.html', context)
