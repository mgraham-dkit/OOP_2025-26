from __future__ import annotations


class Book:
    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    @classmethod
    def from_dict(cls, data):
        try:
            if data["type"] != cls.__name__:
                raise ValueError(f"Invalid type value ({data["type"]}) within dict  - {cls.__name__} cannot deserialise")

            title = data["title"]
            temp_author = data["author"]
            author = Author.from_dict(temp_author)
            return Book(title,author)
        except KeyError as e:
            raise KeyError(f"JSON error occurred when building {cls.__name__} - cannot find key {e}")
            #raise ValueError(f"JSON error occurred when building {cls.__name__} - cannot find key {e}")


class Author:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_dict(cls, data):
        try:
            first = data["first_name"]
            last = data["last_name"]
            return cls(first, last)

        except KeyError as e:
            raise KeyError(f"JSON error occurred when building {cls.__name__} - cannot find key {e}")
            #raise ValueError(f"{cls.__name__} JSON error -> Missing key: {e}")
