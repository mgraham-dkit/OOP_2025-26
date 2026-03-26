from __future__ import annotations


class Book:
    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    @classmethod
    def from_dict(cls, book_dict):
        try:
            title = book_dict["title"]
            temp_author = book_dict["author"]
            author = Author.from_dict(temp_author)
            return Book(title,author)
        except KeyError as e:
            print(f"Issue occurred when building {cls} - cannot find key {e}")
            raise KeyError(f"JSON error occurred when building {cls} - cannot find key {e}")


class Author:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_dict(cls, dict_obj):
        try:
            first = dict_obj["first_name"]
            last = dict_obj["last_name"]
            return cls(first, last)

        except KeyError as e:
            print(f"Issue occurred when building Author - cannot find key {e}")
            raise KeyError(f"JSON error occurred when building {cls} - cannot find key {e}")
