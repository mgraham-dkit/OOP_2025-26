import json
from random import Random

from books import Author


def generate_authors(num_authors: int):
    # Build list of randomly generated Author objects
    random = Random()
    first_names = ["Henry", "Alfred", "Sarah", "Deirdre", "Barry", "Zoey", "Mira"]
    last_names = ["Andrews", "Dunne", "Harris", "Rosenberg", "Chase", "Giles", "Summers"]

    author_list = []
    for i in range(num_authors):
        first_name_index = random.randint(0, len(first_names) - 1)
        last_name_index = random.randint(0, len(last_names) - 1)

        author_obj = Author(first_names[first_name_index], last_names[last_name_index])
        author_list.append(author_obj)

    return author_list

if __name__ == "__main__":
    authors = generate_authors(5)

    # Display the authors so we can check the details are the same in the file!
    for author in authors:
        print(author)

    # JSON COMPONENT BEGINS:::
    # Convert from object to JSON dict
    # Convert each author in the list to a JSON-compatible dictionary
    author_dicts = [author.to_dict() for author in authors]

    # Write to JSON file
    # Output the list of JSON dicts to a file
    with open("authors_output.json", "w") as file:
        json.dump(author_dicts, file, indent=4)
