from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

book_list = {} # like database


class Book(BaseModel):
    author: str
    title: str
    category: Optional[str] = None


class UpdateBook(BaseModel):
    author: Optional[str] = None
    title: Optional[str] = None
    category: Optional[str] = None


@app.get('/')
async def root():
    return {"message": "hello world"}


@app.get('/books/{path_param}')
def first_api(path_param: str):
    return {"message": path_param}


@app.get("/books/")
def query_api(title: str):
    return {"message": title}


@app.get('/books/{path_param}/')
def mix_api(path_param: str, year: int):
    return {"message": [path_param, year]}


@app.post('/books/create_book/')
def create_book(book_id: int, new_book: Book):
    if book_id in book_list:
        return {"msg": "error - book with same id exists"}
    book_list[book_id] = new_book
    return book_list[book_id]


@app.put('/books/update_book/{book_id}')
def update_book(book_id: int, new_book: UpdateBook):
    if book_id not in book_list:
        return {"error": "book id not exists"}

    if new_book.category is not None:
        book_list[book_id].category = new_book.category
    if new_book.title is not None:
        book_list[book_id].title = new_book.title
    if new_book.author is not None:
        book_list[book_id].author = new_book.author
    return book_list[book_id]


@app.delete('/books/delete_book/{book_id}')
def delete_book(book_id: int):
    if book_id in book_list:
        del book_list[book_id]
        return {"msg": "book is deleted"}
    return {"error": "book does not exist"}
