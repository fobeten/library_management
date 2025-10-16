from fastapi import APIRouter
from models import book
from models.book import Book

router = APIRouter(prefix="/books")


@router.get("/")
def get_book():
    return book.get_books()


@router.get("/{id}")
def get_a_book(id: int):
    return book.get_one_book(id)


@router.post("/")
def create_book(new_book: Book):
    return book.add_book(new_book)


@router.put("/{id}")
def put_book(id: int, new_book: Book):
    return book.modify_book_fully(id, new_book)


@router.delete("/{id}")
def remove_book(id: int):
    return book.delete_book(id)