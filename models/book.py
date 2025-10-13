from typing import Optional
from .author import Author


class Book:
    def __init__(self, id: int, title: str, year: int, author: Author):
        self.id = id
        self.title = title
        self.year = year
        self.author = author

    def update(self, title: Optional[str] = None, year: Optional[int] = None) -> None:
        if title is not None:
            self.title = title
        if year is not None:
            self.year = year

    def get_author(self) -> Author:
        return self.author
