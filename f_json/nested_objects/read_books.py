import json
from books import Book

def parse_json(filename: str) -> list[Book]:
    with open(filename) as file:
        list_book_dicts = json.load(file)

        book_list = []
        for book_dict in list_book_dicts:
            book = Book.from_dict(book_dict)
            book_list.append(book)

    return book_list


def display(book_list: list[Book]) -> None:
    for i, book in enumerate(book_list, 1):
        print(f"{i}) {book}")


def main() -> None:
    valid_file = False
    books = []
    while not valid_file:
        filename = input("Enter JSON filename: ")
        try:
            books = parse_json(filename)
            valid_file = True
        except FileNotFoundError as e:
            print(f"File ({e}) not found")
            print("Please try again")

    display(books)


if __name__ == "__main__":
    main()