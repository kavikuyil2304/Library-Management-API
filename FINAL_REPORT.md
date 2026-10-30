# Library Management API — Final Report

## 1. Project Overview
The Library Management API is a RESTful web API developed using Python and FastAPI. It allows users to manage book records through HTTP requests.

## 2. Objectives
- Implement REST API principles.
- Develop CRUD operations for books.
- Return appropriate HTTP status codes.
- Validate incoming request data.
- Test API functionality using automated tests.

## 3. Technologies Used
- Python
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Swagger UI
- Visual Studio Code

## 4. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/books` | Retrieve all books |
| GET | `/api/v1/books/{book_id}` | Retrieve a book by ID |
| POST | `/api/v1/books` | Create a new book |
| PUT | `/api/v1/books/{book_id}` | Update a book |
| DELETE | `/api/v1/books/{book_id}` | Delete a book |

## 5. HTTP Status Codes
- `200 OK` — Request completed successfully.
- `201 Created` — Book created successfully.
- `400 Bad Request` — Duplicate book ID.
- `404 Not Found` — Requested book does not exist.
- `422 Unprocessable Entity` — Request data failed validation.

## 6. Testing
The API was tested using Swagger UI and automated tests using Pytest. The latest recorded test run reported 11 passing tests.

## 7. Limitations
Book records are currently stored in memory. The data may reset when the application restarts. A persistent database has not yet been implemented.

## 8. Future Improvements
- Integrate a persistent database.
- Expand automated test coverage.
- Improve error handling and validation.
- Add authentication if required.

## 9. Conclusion
The project demonstrates the implementation and testing of a versioned REST API using FastAPI, including CRUD operations, request validation, and HTTP status handling.
