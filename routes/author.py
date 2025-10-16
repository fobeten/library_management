from fastapi import APIRouter
from models.author import Author
from models import author

router = APIRouter(prefix="/authors")


@router.get("/")
def get_all_authors():
    return author.get_authors()


@router.get("/{id}")
def get_an_author(id: int):
    return author.get_one_author(id)


@router.get("/books/{id}")
def get_authors_books(id: int):
    return author.get_books(id)


@router.post("/")
def create_author(new_author: Author):
    return author.add_author(new_author)


@router.put("/{id}")
def put_author(id: int, new_author: Author):
    return author.modify_author_fully(id, new_author)


@router.delete("/{id}")
def remove_author(id: int):
    return author.delete_author(id)
