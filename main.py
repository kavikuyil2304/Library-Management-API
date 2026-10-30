from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)



books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "Wings of Fire", "author": "A. P. J. Abdul Kalam"}
]


@app.get("/")
def home():
    return {"message": "Welcome to my Library API!"}


@app.get("/api/v1/books")
def get_books():
    return {"books": books}



@app.post("/api/v1/books", status_code=201)
def add_book(book: Book):
    for existing_book in books:
        if existing_book["id"] == book.id:
            raise HTTPException(
                status_code=400,
                detail="Book ID already exists"
            )

    books.append(book.model_dump())

    return {
        "message": "Book added successfully",
        "book": book
    }



@app.get("/api/v1/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"book": book}

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

@app.put("/api/v1/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = updated_book.model_dump()
            return {
                "message": "Book updated successfully",
                "book": books[index]
            }

    raise HTTPException(
    status_code=404,
    detail="Book not found"
)
    

@app.delete("/api/v1/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

