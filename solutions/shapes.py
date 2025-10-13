class Rectangle:
    # Create a constructor that takes in the length, width and colour
    # for each Rectangle being created
    # Optional parameter (colour) included with a default value of "Blue"
    def __init__(self, length, width, colour="Blue"):
        self.length = length
        self.width = width
        self.colour = colour

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]")

    def calc_area(self):
        return self.length * self.width
