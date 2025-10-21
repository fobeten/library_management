from models.author import Author
from fastapi import HTTPException
from service.book import books

authors = [
    Author(
        id=1,
        name="Chinua Achebe",
        bio="Nigerian novelist and critic",
        books=[],
    ),
    Author(
        id=2,
        name="Jane Austen",
        bio="English novelist known for her romantic fiction",
        books=[],
    ),
    Author(
        id=3,
        name="George Orwell",
        bio="English writer and journalist",
        books=[],
    ),
    Author(
        id=4,
        name="Maya Angelou",
        bio="American poet and civil rights activist",
        books=[],
    ),
    Author(
        id=5,
        name="Haruki Murakami",
        books=[],
    ),
]


def get_author_id():
    return max((a.id for a in authors), default=0) + 1


def get_authors():
    return authors


def get_one_author(author_id: int):
    for author in authors:
        if author.id == author_id:
            book_titles = get_books(author.name)
            return Author(
                id=author.id, name=author.name, bio=author.bio, books=book_titles
            )
    raise HTTPException(status_code=404, detail="That Author doesn't exist")


def get_books(author_name: str):
    book_titles = []
    # author_name = None
    # for author in authors:
    #     if author_id == author.id:
    #         author_name = author.name

    if author_name is None:
        return []

    for book in books:
        if author_name.lower() == book.author.lower():
            book_titles.append(book.title)
    return book_titles


# print(get_books("Haruki Murakami"))


def add_author(author: Author):
    new_author = Author(
        id=get_author_id(), name=author.name, bio=author.bio, books=author.books
    )

    authors.append(new_author)
    return new_author


def modify_author_fully(author_id: int, updated_author: Author):
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


def delete_author(id: int):
    global authors
    for i, author in enumerate(authors):
        if author.id == id:
            authors.pop(i)
            return f"Author {author.name} was deleted"
    raise HTTPException(status_code=404, detail="Author not found")
