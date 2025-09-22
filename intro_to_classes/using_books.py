from books import Book

book1 = Book()
print(f"{book1.title} by {book1.author}")

book2 = Book()
print(f"(Before) {book2.title} by {book2.author}")
book2.title = "Alice in Wonderland"
book2.author = "Lewis Carroll"
print(f"(after) {book2.title} by {book2.author}")
print(f"Book1: {book1.title} by {book1.author}")