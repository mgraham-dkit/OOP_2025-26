class Person:
    def __init__(self, first, last, age, left_handed):
        self.first = first
        self.last = last
        self.age = age
        self.left_handed = left_handed

    def display(self):
        if self.left_handed:
            print(f"{self.first} {self.last}")
        else:
            print(f"{self.first.upper()} {self.last.upper()}")