
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_all_books():
    response = client.get("/api/v1/books")
    assert response.status_code == 200


def test_book_not_found():
    response = client.get("/api/v1/books/999")
    assert response.status_code == 404


def test_duplicate_book_id():
    response = client.post(
        "/api/v1/books",
        json={
            "id": 1,
            "title": "Duplicate Test",
            "author": "Test Author"
        }
    )
    assert response.status_code == 400

def test_delete_book_not_found():
    response = client.delete("/api/v1/books/999")
    assert response.status_code == 404

def test_successful_book_creation():
    response = client.post(
        "/api/v1/books",
        json={
            "id": 100,
            "title": "New Test Book",
            "author": "Test Author"
        }
    )
    assert response.status_code == 201
    assert "New Test Book" in response.text

def test_successful_book_update():
    response = client.put(
        "/api/v1/books/1",
        json={
            "id": 1,
            "title": "Updated Alchemist",
            "author": "Paulo Coelho"
        }
    )
    assert response.status_code == 200
    assert "Updated Alchemist" in response.text

def test_successful_book_deletion():
    response = client.delete("/api/v1/books/2")
    assert response.status_code == 200
    assert "Book deleted successfully" in response.text

def test_invalid_book_id():
    response = client.post(
        "/api/v1/books",
        json={
            "id": 0,
            "title": "Invalid Book",
            "author": "Test Author"
        }
    )
    assert response.status_code == 422


def test_empty_book_title():
    response = client.post(
        "/api/v1/books",
        json={
            "id": 101,
            "title": "",
            "author": "Test Author"
        }
    )
    assert response.status_code == 422

def test_update_book_not_found():
    response = client.put(
        "/api/v1/books/999",
        json={
            "id": 999,
            "title": "Missing Book",
            "author": "Test Author"
        }
    )
    assert response.status_code == 404


def test_delete_book_not_found():
    response = client.delete("/api/v1/books/999")
    assert response.status_code == 404
