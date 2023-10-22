from fastapi.testclient import TestClient

from ..src.main import app  # need to add __init__.py at the same level as src,tests,and venv folder to import like this

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}

def test_first_api():
    response = client.get("/books/title")
    assert response.status_code == 200
    assert response.json() == {"message": "title"}

def test_query_api():
    response = client.get("/books/?title=harry potter")
    assert response.status_code == 200
    assert response.json() == {"message": "harry potter"}

def test_mix_api():
    response = client.get('/books/harry/?year=2020')
    assert response.status_code == 200
    assert response.json() == {"message": ["harry", 2020]}

def test_create_book():
    response = client.post('/books/create_book/?book_id=1',
                           json={
                               "title": "Bazz",
                               "author": "Drop the bazz",
                               "category": "fiction"
                           })
    assert response.status_code == 200
    assert response.json() == {
                               "title": "Bazz",
                               "author": "Drop the bazz",
                               "category": "fiction"
                           }

def test_update_book():
    response = client.put('/books/update_book/1', json={"category": "non-fiction"})
    assert response.status_code == 200
    assert response.json() == {
        "title": "Bazz",
        "author": "Drop the bazz",
        "category": "non-fiction"
    }

def test_delete_book():
    response = client.delete('/books/delete_book/1')
    assert response.status_code == 200
    assert response.json() == {"msg": "book is deleted"}

    response = client.delete('/books/delete_book/4')
    assert response.status_code == 200
    assert response.json() == {"error": "book does not exist"}

