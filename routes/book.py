from fastapi import APIRouter
from models.book import Book
import services.book as service

router = APIRouter(prefix="/books")


@router.get("/")
def get_book():
    return service.get_all_books()


@router.get("/{id}")
def get_a_book(id: int):
    return service.get_one_book(id)


@router.post("/")
def create_book(new_book: Book):
    return service.add_book(new_book)


@router.put("/{id}")
def put_book(id: int, new_book: Book):
    return service.modify_book_fully(id, new_book)


@router.delete("/{id}")
def remove_book(id: int):
    return service.delete_book(id)
