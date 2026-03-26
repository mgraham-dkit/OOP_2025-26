import json
from books import Author


with open("authors.json") as file:
    authors_dict_list = json.load(file)

    authors = []
    for author_dict in authors_dict_list:
        author = Author.from_dict(author_dict)
        authors.append(author)

    for author in authors:
        print(author)