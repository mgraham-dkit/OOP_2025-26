from people import Person


people = []
for i in range(5):
    # Take in information to create a person
    first_name = input(f"Please enter first name: ")
    last_name = input(f"Please enter last name: ")
    age = int(input(f"Please enter age: "))
    choice = input(f"Are you left handed? (y for yes, any other key for no): ")

    if choice.lower() == "y":
        handed = True
    else:
        handed = False

    person = Person(first_name, last_name, age, handed)
    people.append(person)

for p in people:
    p.display()