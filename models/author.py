from os import name
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from models.book import get_next_id

app = FastAPI()

class Author(BaseModel):
    id:int = None
    name:str
    bio: Optional[str] = None
    books:List[str] = []


authors = [
    Author(
        id=1,
        name="Chinua Achebe",
        bio="Nigerian novelist and critic",
        books=["Things Fall Apart", "No Longer at Ease"],
    ),
    Author(
        id=2,
        name="Jane Austen",
        bio="English novelist known for her romantic fiction",
        books=["Pride and Prejudice", "Sense and Sensibility", "Emma"],
    ),
    Author(
        id=3,
        name="George Orwell",
        bio="English writer and journalist",
        books=["1984", "Animal Farm"],
    ),
    Author(
        id=4,
        name="Maya Angelou",
        bio="American poet and civil rights activist",
        books=["I Know Why the Caged Bird Sings"],
    ),
    Author(
        id=5,
        name="Haruki Murakami",
        books=["Norwegian Wood", "Kafka on the Shore", "1Q84"],
    ),
]

def get_author_id():
    return max((a.id for a in authors), default=0) + 1

print(get_author_id())

def get_authors():
    return authors

def get_one_author(author_id:int):
    for author in authors:
        if author.id == author_id:
            return author
    raise HTTPException(status_code=404, detail="That Author doesn't exist")

def get_books(author_id:int):
    for author in authors:
        if author.id == author_id:
            return author.books
    raise HTTPException(status_code=404, detail="That Author doesn't exist")

def add_author(author:Author):
    new_author = Author(
        id = get_author_id(),
        name = author.name,
        bio = author.bio,
        books = author.books
    )

    authors.append(new_author)
    return new_author


def fully_update_author(author_id: int, updated_author: Author):
    for i, author in enumerate(authors):
        if author.id == author_id:
            authors[i] = Author(
                id=author_id,
                name=updated_author.name,
                bio=updated_author.bio,
                books=updated_author.books,
            )
            return authors[i]
    raise HTTPException(status_code=404, detail="Author not found")


@app.get("/authors")
def get_all_authors():
    return get_authors()

@app.get("/authors/{id}")
def get_an_author(id:int):
    return get_one_author(id)

@app.get("/authorsbooks/{id}")
def get_authors_books(id:int):
    return get_books(id)

@app.post("/authors")
def create_author(author:Author):
    return add_author(author)
