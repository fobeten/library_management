# Library Management System

A RESTful API for managing a library's books and authors, built with FastAPI and Python. This system provides endpoints for creating, reading, updating, and deleting (CRUD) both books and authors.

## Features

- **Author Management**: Create, read, update, and delete author records with biographical information
- **Book Management**: Manage book records including title, publication year, and author
- **Author-Book Relationship**: View all books written by a specific author
- **In-Memory Storage**: Uses in-memory data storage for quick prototyping and testing
- **RESTful API**: Clean and intuitive API endpoints following REST principles
- **Automatic API Documentation**: Interactive API documentation via FastAPI's built-in Swagger UI

## Tech Stack

- **Python 3.x**
- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: Lightning-fast ASGI server

## Project Structure

```
library_management/
├── main.py                 # Application entry point
├── storage.py             # In-memory data storage and business logic
├── requirements.txt       # Python dependencies
├── models/
│   ├── __init__.py
│   ├── author.py         # Author data model
│   └── book.py           # Book data model
└── routes/
    ├── __init__.py
    ├── author.py         # Author API endpoints
    └── book.py           # Book API endpoints
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/fobeten/library_management.git
   cd library_management
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

   The `--reload` flag enables auto-reload on code changes (useful for development).

2. **Access the application**
   - API Base URL: `http://127.0.0.1:8000`
   - Interactive API Documentation (Swagger UI): `http://127.0.0.1:8000/docs`
   - Alternative API Documentation (ReDoc): `http://127.0.0.1:8000/redoc`

3. **To run on a different port**
   ```bash
   uvicorn main:app --reload --port 8080
   ```

4. **To make the server accessible from other devices on your network**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0
   ```

## API Endpoints

### Authors

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/authors/` | Get all authors |
| GET | `/authors/{id}` | Get a specific author by ID |
| GET | `/authors/books/{author_name}` | Get all books by an author |
| POST | `/authors/` | Create a new author |
| PUT | `/authors/{id}` | Update an author |
| DELETE | `/authors/{id}` | Delete an author |

### Books

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Get all books |
| GET | `/books/{id}` | Get a specific book by ID |
| POST | `/books/` | Create a new book |
| PUT | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |

## Usage Examples

### Create a New Author
```bash
curl -X POST "http://127.0.0.1:8000/authors/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "J.K. Rowling",
    "bio": "British author best known for the Harry Potter series"
  }'
```

### Create a New Book
```bash
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Harry Potter and the Philosopher Stone",
    "year": 1997,
    "author": "J.K. Rowling"
  }'
```

### Get All Books by an Author
```bash
curl "http://127.0.0.1:8000/authors/books/George%20Orwell"
```

### Get a Specific Author
```bash
curl "http://127.0.0.1:8000/authors/1"
```

## Sample Data

The application comes pre-loaded with sample data:

**Authors:**
- Chinua Achebe
- Jane Austen
- George Orwell
- Maya Angelou
- Haruki Murakami

**Books:**
- Things Fall Apart (1958)
- Pride and Prejudice (1813)
- 1984 (1949)
- Animal Farm (1945)
- I Know Why the Caged Bird Sings (1969)
- Norwegian Wood (1987)
- Kafka on the Shore (2002)

## Data Models

### Author
```python
{
  "id": int,
  "name": str,
  "bio": str (optional),
  "books": List[str]
}
```

### Book
```python
{
  "id": int,
  "title": str,
  "year": int,
  "author": str
}
```

## Development

### Running Tests
*Note: Test suite not yet implemented*

### Code Style
This project follows standard Python conventions (PEP 8).

## Future Enhancements

- [ ] Add database integration (PostgreSQL/MongoDB)
- [ ] Implement user authentication and authorization
- [ ] Add book borrowing/lending functionality
- [ ] Implement search and filtering capabilities
- [ ] Add pagination for large datasets
- [ ] Add input validation and error handling improvements
- [ ] Implement unit and integration tests
- [ ] Add book categories/genres
- [ ] Include ISBN tracking for books

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or feedback, please open an issue on the GitHub repository.

---

**Note**: This application uses in-memory storage, meaning all data will be lost when the server restarts. For production use, consider implementing persistent database storage.
