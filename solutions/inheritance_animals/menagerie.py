import random

from animals import Animal, Dog


def create_animal() -> Animal:
    # Take in the parts of the animal
    name = input("What is this Animal's name? ")
    dob = input(f"Please enter {name}'s date of birth (format: dd/mm/yy): ")
    weight = float(input(f"Please enter {name}'s weight (in kg): "))

    # Create a new Animal object and return it to the script/program
    return Animal(dob, weight, name)

def display_animals(animal_list: list[Animal]) -> None:
    # Loop through every animal in supplied list
    for current_animal in animal_list:
        # Ask it to show its information on console
        current_animal.display()
        print()

def get_below_age(animal_list: list[Animal], age: int) -> list[Animal]:
    # Create a list to hold all animals with age <= specified age
    matches = []
    # Check each animal in list
    for current_animal in animal_list:
        # If this animal is correct age
        if current_animal.calc_age() <= age:
            # Add this animal to the matches list
            matches.append(current_animal)

    # Return list of matches
    return matches


if __name__ == "__main__":
    # Create three hard-coded animals
    animalA = Animal("13/09/13", 3.5, "Fido")
    animal_negative_weight = Animal("10/08/22", -10, "Hungry boi")
    animal_None_dob = Animal(None, 4.21, "Ricky")
    # Add to list
    animals = [animalA, animal_negative_weight, animal_None_dob]

    # Create two user-defined animals and add to list
    for i in range(2):
        animal = create_animal()
        animals.append(animal)

    # Create two hard-coded Dog objects and add to list
    dog1 = Dog("14/03/24", 2.23, "Chihuahua","Jackson", "Yappy")
    animals.append(dog1)
    dog2 = Dog("24/07/21", 5.18, "Poodle", "Bruiser", "Aggressive")
    animals.append(dog2)

    # Shuffle the list of animals
    random.shuffle(animals)

    # Display the animal list
    print("-----------------------")
    print("       Animals:")
    display_animals(animals)
    print("-----------------------")

    # Display all animals aged 2 or younger
    age = 2
    # Find all animals 2 or younger
    animals_under_age = get_below_age(animals, age)
    # Display them
    print("---------------------------------")
    print(f"  Animals aged {age} or under: ")
    print("---------------------------------")
    display_animals(animals_under_age)