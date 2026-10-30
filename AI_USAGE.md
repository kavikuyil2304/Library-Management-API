# AI Tools and Usage

## 1. AI Tool Used
- **Tool:** ChatGPT

## 2. Purpose of Using AI
ChatGPT was used as an assistant during the development of the Library Management API.

## 3. Tasks Supported by AI
- Understanding REST API principles and HTTP status codes.
- Implementing and debugging FastAPI endpoints.
- Understanding request validation using Pydantic.
- Creating automated tests using Pytest.
- Troubleshooting errors and interpreting test results.
- Preparing project documentation and the design checklist.

## 4. Example Prompts Used
- How do I implement CRUD endpoints using FastAPI?
- How do I return appropriate HTTP status codes?
- How do I validate book IDs and request data?
- How do I write automated tests for API endpoints?
- How do I troubleshoot errors in my Python code?

## 5. Errors and Corrections
During development, errors such as indentation issues, duplicate book ID responses, and test assertion failures were investigated and corrected with assistance from ChatGPT.

## 6. Verification
The API endpoints were tested using Swagger UI, and automated tests were run using Pytest. The latest test run reported 11 passing tests.

## 7. Declaration
AI was used as a development aid. The project code and test results were reviewed and verified during implementation.
## AI Tool Usage – Google Gemini

**Tool:** Google Gemini

**Purpose:** Research on REST API principles, HTTP methods, API versioning, OpenAPI documentation and HTTP status codes.

**Task performed:** Asked Gemini to explain five core API design concepts using examples from a Library Management API.

**Outcome:** The response provided explanations and examples for GET, POST, PUT, DELETE, API versioning, Swagger UI, OpenAPI and HTTP status codes.

**Verification:** The generated explanations were reviewed against official FastAPI, MDN and OpenAPI documentation. One correction was identified: FastAPI's default request validation response is generally HTTP 422, not HTTP 400. The project's duplicate-book-ID error uses a custom HTTP 400 response.

**Responsible AI practice:** AI-generated information was reviewed and checked against reliable documentation before use.
## AI Tool Usage – Claude

**Tool:** Claude (Anthropic)

**Purpose:** Review the REST API design and identify improvements.

**Task performed:** Submitted the Library Management API endpoint structure and requested feedback on REST principles, HTTP status codes, validation, error handling, security, reliability and testing.

**Key findings:**
- The resource-oriented endpoint structure follows common REST conventions.
- PUT should be documented as a full update operation.
- Separate request and response schemas could improve data handling.
- Input validation should reject whitespace-only strings and enforce suitable length limits.
- A Location header can improve POST responses.
- Persistent database storage, authentication, logging and pagination are possible future enhancements.

**Verification:** Suggestions were compared with the existing FastAPI implementation. Recommendations were treated as proposed improvements, not as implemented features.

**Responsible AI practice:** Reviewed the AI-generated recommendations and retained the existing implementation details accurately.
## AI Tool Usage – DeepSeek

**Tool:** DeepSeek

**Purpose:** Develop a verification and testing plan for the Library Management API.

**Task performed:** Requested a practical plan to verify CRUD endpoints, HTTP status codes, invalid inputs, OpenAPI documentation accuracy, AI-generated code correctness, security and hallucinated claims.

**Key findings:**
- Verify all CRUD operations using automated and manual tests.
- Check both HTTP status codes and response bodies.
- Test missing fields, invalid types and malformed JSON.
- Compare implemented API routes with the OpenAPI specification.
- Maintain timestamped test evidence and defect logs.
- Independently verify AI-generated code and security claims.

**Verification:** This output is a proposed testing plan. It does not mean all suggested tests or security checks have been executed.

**Responsible AI practice:** Recommendations will be checked against the actual FastAPI implementation before being reported as completed.
