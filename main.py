from fastapi import FastAPI

from routes import author, book


app = FastAPI()

app.include_router(book.router)
app.include_router(author.router)

@app.get('/')
def home():
    return "Home Page"