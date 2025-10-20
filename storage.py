from models.author import Author
from models.book import Book
from fastapi import HTTPException

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


books = [
    Book(id=1, title="Things Fall Apart", year=1958, author="Chinua Achebe"),
    Book(id=2, title="Pride and Prejudice", year=1813, author="Jane Austen"),
    Book(id=3, title="1984", year=1949, author="George Orwell"),
    Book(id=4, title="Animal Farm", year=1945, author="George Orwell"),
    Book(
        id=5, title="I Know Why the Caged Bird Sings", year=1969, author="Maya Angelou"
    ),
    Book(id=6, title="Norwegian Wood", year=1987, author="Haruki Murakami"),
    Book(id=7, title="Kafka on the Shore", year=2002, author="Haruki Murakami"),
]

def get_author_id():
    return max((a.id for a in authors), default=0) + 1


def get_authors():
    return authors


def get_one_author(author_id: int):
    for author in authors:
        if author.id == author_id:
            return author
    raise HTTPException(status_code=404, detail="That Author doesn't exist")


def get_books(author_id:int):
    book_titles = []
    author_name = None
    for author in authors:
        if author_id == author.id:
            author_name = author.name
        
    if author_name is None:
        return []
    
    for book in books:
        if author_name.lower() == book.author.lower():
            book_titles.append(book.title)
    return book_titles

print(get_books(5))

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


"""BOOK LOGIC"""

def get_next_id():
    return max((b.id for b in books), default=0) + 1


def get_all_books():
    return books


def get_one_book(book_id: int):
    for book in books:
        if book_id == book.id:
            return book.model_dump()
    raise HTTPException(status_code=404, detail="book doesn't exist")


def add_book(book: Book):
    new_book = Book(
        id=get_next_id(), title=book.title, year=book.year, author=book.author
    )
    books.append(new_book)
    return new_book


def modify_book_fully(book_id: int, updated_book: Book):
    for i, author in enumerate(books):
        if author.id == book_id:
            books[i] = Book(
                id=book_id,
                title=updated_book.title,
                year=updated_book.year,
                author=updated_book.author,
            )
            return books[i]
    raise HTTPException(status_code=404, detail="Author not found")


def delete_book(id: int):
    global books
    for i, book in enumerate(books):
        if book.id == id:
            books.pop(i)
            return f"Book {book.title} was deleted"
    raise HTTPException(status_code=404, detail="Author not found")
