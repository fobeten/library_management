from models.book import Book
from fastapi import HTTPException

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