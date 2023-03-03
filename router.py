from fastapi import APIRouter
import service
from schema import Book


book_app = APIRouter()


@book_app.get("/")
def get_all_books():
    return service.get_books()


@book_app.get("/{book_id}")
def get_one_book(book_id: int):
    return service.get_book(book_id)


@book_app.post("/")
def create_book(book: Book):
    return service.add_book(book)


@book_app.put("/{book_id}")
def custom_book(book_id: int, book: Book):
    return service.update_book(book_id, book)


@book_app.delete("/{book_id}")
def delete_book(book_id: int):
    return service.remove_book(book_id)
