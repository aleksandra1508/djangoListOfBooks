import requests

from books.models import Book


def imported_books(queries):
    clean_queries = {}
    for k, v in queries.items():
        if v != '':
            clean_queries[k] = v
    queries = clean_queries
    url = 'https://www.googleapis.com/books/v1/volumes?'

    if 'q' in queries:
        url += f"q={queries['q']}"
    else:
        url += f"q="
    if 'title' in queries:
        url += f"+intitle:{queries['title']}"
    if 'author' in queries:
        url += f"+inauthor:{queries['author']}"
    if 'isbn' in queries:
        url += f"+isbn:{queries['isbn']}"

    get_books = requests.get(url)

    return get_books.json()


def json_to_list(books):
    books = books['items']
    import_books = []
    if books:
        for book in books:
            volume = book['volumeInfo']
            import_book = Book(title=volume['title'], author=(lambda x: volume[x] if(x in volume) else "")('authors'),
                               date_of_publication=(lambda x: volume[x] if(x in volume) else "")('publishedDate'),
                               isbn=volume['industryIdentifiers'][0]['identifier'],
                               number_of_pages=(lambda x: volume[x] if(x in volume) else 0)('pageCount'),
                               image_link=(lambda x: volume['imageLinks'][x]
                               if('imageLinks' in volume and x in volume['imageLinks'])
                               else None)('thumbnail'),
                               language=volume['language'])
            import_books.append(import_book)
    return import_books
