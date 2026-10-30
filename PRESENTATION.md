
# Library Management API — Presentation

## Slide 1: Title and Project Overview

**Library Management API**

- Capstone Project
- Developed using Python and FastAPI
- REST API to manage library books.
- Supports creating, viewing, updating and deleting books.

## Slide 2: Technologies Used

- Python – Programming language
- FastAPI – API development framework
- Pydantic – Request data validation
- Uvicorn – Application server
- Pytest – Automated testing
- Swagger UI – Interactive API documentation

## Slide 3: REST API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/books` | Get all books |
| GET | `/api/v1/books/{book_id}` | Get a specific book |
| POST | `/api/v1/books` | Create a book |
| PUT | `/api/v1/books/{book_id}` | Update a book |
| DELETE | `/api/v1/books/{book_id}` | Delete a book |

## Slide 4: Validation and HTTP Status Codes

**Data Validation**
- Book IDs must be positive integers.
- Book titles cannot be empty.
- Author names cannot be empty.
- Pydantic validates incoming request data.

**HTTP Status Codes**
- 200 – Request successful
- 201 – Book created
- 400 – Duplicate book ID
- 404 – Book not found
- 422 – Invalid request data

## Slide 5: Testing and Verification

- Automated tests written using Pytest.
- Latest recorded test run: 11 tests passed.
- API endpoints tested using Swagger UI.
- OpenAPI automation verification: SUCCESS.
- All 6 registered API endpoints match OpenAPI documentation.

## Slide 6: Limitations, Future Improvements and Conclusion

**Limitations**
- Book data is stored in memory.
- Data resets when the server restarts.

**Future Improvements**
- Integrate a persistent database.
- Add authentication and authorization.
- Expand automated testing.

**Conclusion**
- Implemented CRUD operations using FastAPI.
- Added data validation, HTTP error handling and API documentation.

**Thank You!**
