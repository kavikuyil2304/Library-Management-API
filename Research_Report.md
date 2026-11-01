
# Research Report
## Library Management REST API Using FastAPI

### 1. Introduction

A Library Management API is a software application designed to manage book information through REST API operations. This project uses Python and FastAPI to create an API that supports basic book management operations.

### 2. Problem Statement

Managing book information manually can be difficult. A structured API is needed to retrieve, add, update and delete book records efficiently.

### 3. Project Objectives

- Develop a REST API using FastAPI.
- Implement CRUD operations for books.
- Validate incoming data using Pydantic.
- Handle errors using HTTP status codes.
- Generate interactive API documentation.
- Test API functionality using Pytest.
- Verify API routes against OpenAPI documentation.

### 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API development |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| Pytest | Automated testing |
| Swagger UI | API documentation |

### 5. REST API Design

The project follows resource-oriented API design.

| Method | Endpoint | Operation |
|---|---|---|
| GET | /api/v1/books | Retrieve all books |
| GET | /api/v1/books/{book_id} | Retrieve one book |
| POST | /api/v1/books | Create a book |
| PUT | /api/v1/books/{book_id} | Update a book |
| DELETE | /api/v1/books/{book_id} | Delete a book |

### 6. Implementation

The application uses FastAPI to define API routes and Pydantic models to validate book information.

Each book contains:
- ID
- Title
- Author

The application supports creating, retrieving, updating and deleting book records.

### 7. HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Book created |
| 400 | Duplicate book ID |
| 404 | Book not found |
| 422 | Invalid request data |

### 8. API Documentation

FastAPI automatically generates API documentation.

- Swagger UI: /docs
- ReDoc: /redoc
- OpenAPI JSON: /openapi.json

These interfaces help developers understand and test API endpoints.

### 9. Testing and Verification

Pytest is used to execute automated tests.

The project also includes an OpenAPI verification script.

The recorded verification result confirms that all six registered API routes match the OpenAPI documentation.

The latest recorded automated test result was 11 passed tests.

### 10. Limitations

- Book records are stored in an in-memory Python list.
- Data is lost when the server restarts.
- Database integration is not implemented.
- Authentication and authorization are not implemented.
- Pagination and advanced search are not implemented.

### 11. Future Enhancements

- Integrate SQLite or PostgreSQL.
- Add user authentication.
- Introduce librarian and user roles.
- Implement pagination and search.
- Expand automated testing.

### 12. Conclusion

The Library Management REST API demonstrates the development of a basic API using Python and FastAPI. It implements CRUD operations, request validation, HTTP error handling, automated testing and OpenAPI documentation.

The project provides a foundation for developing a more complete library management system.

### 13. References

1. FastAPI Documentation: https://fastapi.tiangolo.com/
2. Pydantic Documentation: https://docs.pydantic.dev/
3. Python Documentation: https://docs.python.org/3/
4. Pytest Documentation: https://docs.pytest.org/
5. MDN HTTP Methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
6. OpenAPI Specification: https://spec.openapis.org/oas/latest.html
