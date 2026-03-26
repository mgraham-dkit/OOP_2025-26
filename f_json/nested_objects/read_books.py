import json
from books import Book


with open("book.json") as file:
    book_dict = json.load(file)

    book = Book.from_dict(book_dict)
    print(book)