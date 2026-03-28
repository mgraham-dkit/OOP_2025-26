import json
from random import Random
from books import Author
from books import Book
from writing_authors import generate_authors

def generate_books(num_books: int) -> list[Book]:
    authors = generate_authors(num_books)

    titles = ["Disclosure", "The Odyssey", "Peppa Porcupine", "Blue Heeler Industries", "Alias Investigations", "War of the Worlds", "Jurassic Park"]

    book_list = []
    random = Random()
    for i in range(num_books):
        title_index = random.randint(0, len(titles)-1)

        book = Book(titles[title_index], authors[i])
        book_list.append(book)

    return book_list


if __name__ == "__main__":
    books = generate_books(5)

    # Display the authors so we can check the details are the same in the file!
    for book in books:
        print(book)

    # JSON COMPONENT BEGINS:::
    # Convert from object to JSON dict
    # Convert each book in the list to a JSON-compatible dictionary
    book_dicts = [book.to_dict() for book in books]

    # Write to JSON file
    # Output the list of JSON dicts to a file
    with open("books_output.json", "w") as file:
        json.dump(book_dicts, file, indent=4)