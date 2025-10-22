from fastapi import APIRouter
from models.author import Author
import services.author as service


router = APIRouter(prefix="/authors")


@router.get("/")
@router.get("")
def get_all_authors():
    return service.get_authors()


@router.get("/{id}")
def get_an_author(id: int):
    return service.get_one_author(id)


@router.get("/books/{author_name}")
def get_authors_books(author_name: str):
    return service.get_books(author_name)


@router.post("/")
def create_author(new_author: Author):
    return service.add_author(new_author)


@router.put("/{id}")
def put_author(id: int, new_author: Author):
    return service.modify_author_fully(id, new_author)


@router.delete("/{id}")
def remove_author(id: int):
    return service.delete_author(id)
