from people import Person

def display(person):
    if person.left_handed:
        print(f"{person.first} {person.last}")
    else:
        print(f"{person.first.upper()} {person.last.upper()}")


person1 = Person("Joe", "Bloggs", 30, False)

person1.display()

first_name = input(f"Please enter first name: ")
last_name = input(f"Please enter last name: ")
age = int(input(f"Please enter age: "))
choice = input(f"Are you left handed? (y for yes, any other key for no): ")

if choice.lower() == "y":
    handed = True
else:
    handed = False

person2 = Person(first_name, last_name, age, handed)

person2.display()

person3 = Person(first_name, last_name, age, handed)
person3.display()

people = []
for i in range(3):
    person = Person(f"Joe{i}", "Bloggs", 30, False)
    people.append(person)
    
for p in people:
    print(p)
    
    