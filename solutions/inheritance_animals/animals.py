from datetime import datetime


class Animal:
    def __init__(self, dob: str, weight: float, name:str = "Harold"):
        if name is None:
            name = "Harold"
        self.name = name

        if weight < 0:
            print("Cannot have a negative weight!! Defaulting to 5kg")
            weight = 5
        self.weight = weight

        # If None passed in for dob, create text representation of now
        if dob is None:
            dob = datetime.now().strftime("%d/%M/%y")
        # Convert string date representation to datetime object
        self.dob = datetime.strptime(dob, "%d/%M/%y")

        # If calculated age is less than 0 (i.e. dob is after now)
        # set date of birth to today
        if self.calc_age() < 0:
            self.dob = datetime.now()

    def display(self) -> None:
        print(f"{self.__class__.__name__}:")
        print(f"Name:\t\t {self.name}")
        print(f"Age:\t\t {self.calc_age()}")
        print(f"Weight:\t\t {self.weight}")

    def calc_age(self) -> int:
        # Get today's date and time
        now = datetime.now()

        # Calculate different between now and animals' date of birth in days
        age = (now - self.dob).days
        # Divide the age in days by 365 (rounded down to whole integer) to get age in years
        return age // 365


class Dog(Animal):
    def __init__(self, dob: str, weight: float, breed:str, name:str = "Harold", personality: str = "Happy"):
        super().__init__(dob, weight, name)
        self.breed = breed
        if not personality:
            personality = "Happy"
        self.personality = personality

    def display(self) -> None:
        super().display()
        print(f"Breed:\t {self.breed}")
        print(f"Personality: {self.personality}")


if __name__ == "__main__":
    animalA = Animal("13/09/13", 3.5, "Fido")
    print(f"{animalA.name}'s age: {animalA.calc_age()}")

    animal_negative_weight = Animal("10/08/22", -10, "Hungry boi")
    animal_negative_weight.display()

    animal_None_dob = Animal(None, 4.21, "Ricky")
    animal_None_dob.display()
    print(f"{animal_None_dob.name}'s date of birth is {animal_None_dob.dob}")