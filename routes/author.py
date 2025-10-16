from fastapi import APIRouter
from models.author import Author

router = APIRouter(prefix="/author")


@router.get("/")
def all_authors() -> Author:
    return Author.get_books()