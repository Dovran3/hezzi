from database import DB
from schema import Book


def get_books():
    result = DB.select(
        '''
            SELECT * FROM books
        '''
    )

    return result

def get_book(id: int):
    result = DB.select_one(
        '''
            SELECT * FROM books where id=%(id)s
        ''',
        {'id': id}
    )

    return result

def add_book(book: Book):
    DB.execute(
        '''
            INSERT INTO books (title, author) VALUES (
                %s, %s
            )
        ''',
        (book.title, book.author)
    )

def update_book(id: int, book: Book):
    DB.execute(
        '''
            UPDATE books SET (title, author) = (%s, %s) where id=%s
        ''',
        (book.title, book.author, id)
    )

def remove_book(id: int):
    DB.execute(
        '''
            DELETE FROM books where id=%s
        ''',
        (id,)
    )
