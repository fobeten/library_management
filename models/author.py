from typing import List, Optional
from .book import Book

class Author:
    def __init__(self, id: int, name: str, bio: Optional[str] = None):
        self.id = id
        self.name = name
        self.bio = bio
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)

    def get_books(self) -> List[Book]:
        return self.books