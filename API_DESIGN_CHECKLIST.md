
# Library Management API — Design Checklist

## 1. REST API Principles
- [x] Resources use clear names: `/books`
- [x] HTTP methods represent actions: GET, POST, PUT, DELETE
- [x] API endpoints use versioning: `/api/v1/`
- [ ] Use appropriate HTTP status codes for every outcome
- [ ] Use a database for persistent book storage

## 2. HTTP Status Codes
- [x] 200 OK — Request successful
- [x] 400 Bad Request — Duplicate book ID
- [x] 404 Not Found — Book does not exist
- [x] 201 Created — Book successfully created
- [ ] 500 Internal Server Error — Unexpected server errors

## 3. API Documentation
- [x] FastAPI Swagger UI: `/docs`
- [x] OpenAPI JSON specification: `/openapi.json`
- [x] Endpoint request and response schemas documented
- [x] Verify documentation matches implemented behaviour

## 4. Testing
- [x] Home endpoint test
- [x] Get all books test
- [x] Book not found test
- [x] Duplicate book ID test
- [x] Test successful book creation
- [x] Test successful book update
- [x] Test successful book deletion

## 5. Reliability and Security
- [x] Validate book IDs and request data
- [ ] Avoid exposing sensitive information
- [ ] Verify all error responses
- [ ] Confirm data persistence after restarting the server

## 6. Final Review
- [ ] Review REST design decisions
- [x] Verify OpenAPI specification
- [x] Document AI tools and prompts used
- [x] Record AI-generated errors and corrections
- [x] Prepare final report, quiz and presentation
