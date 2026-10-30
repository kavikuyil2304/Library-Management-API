
# Library Management API

## Project Overview
A REST API built using FastAPI to manage library books.

## Features
- Get all books
- Get a book by ID
- Add a new book
- Update book details
- Delete a book
- Handle duplicate book IDs and missing books

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Pytest

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python -m uvicorn main:app --reload
```

Open Swagger documentation:

http://127.0.0.1:8000/docs

## Run Tests

```bash
python -m pytest -v --ignore=test_results.txt
```

## Test Results
5 automated tests passed.
