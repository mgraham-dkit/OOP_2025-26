from people import Person

def display(person):
    if person.left_handed:
        print(f"{person.first} {person.last}")
    else:
        print(f"{person.first.upper()} {person.last.upper()}")


# Create a Person object with hard-coded data
# This will call the __init__ method of the Person class and pass the specified values
# into its variables
person1 = Person("Joe", "Bloggs", 30, False)

# Display person1
# This will call the display() method for person1 - only person1 will be involved in this
person1.display()

# Take in information to create a person
first_name = input(f"Please enter first name: ")
last_name = input(f"Please enter last name: ")
age = int(input(f"Please enter age: "))
choice = input(f"Are you left handed? (y for yes, any other key for no): ")

if choice.lower() == "y":
    handed = True
else:
    handed = False

# Create a Person object with user-supplied information
# Same approach as for hard-coded but the values are entered by the user
# __init__ is still triggered and the values are still set into the object's variables
person2 = Person(first_name, last_name, age, handed)

# Call the display method for person2
# This will call the display method for person2, no other Person objects will be involved
person2.display()

# Create and store multiple Person objects
# Step 1: Create a list to store Person objects
people = []
# Step 2: Loop x times (if you know you want X Persons)
for i in range(3):
    # Step 3: Create a Person object with hard-coded information
    person = Person(f"Joe{i}", "Bloggs", 30, False)
    # Step 4: Add that person to the list
    people.append(person)

# To loop through all person objects in a list
for p in people:
    # Print the current person object from the list
    # Note: THIS DOES NOT DO WHAT YOU THINK IT DOES!
    print(p)
    