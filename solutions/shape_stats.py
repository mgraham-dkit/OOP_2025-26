from shapes import Rectangle


# Function to create a new rectangle based on user input
def create_rectangle():
    print("Now creating a rectangle!")
    # Take in the components to make a rectangle
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    colour = input("Enter colour: ")

    # Build a rectangle from the supplied values
    user_rectangle = Rectangle(length, width, colour)

    # Return the new rectangle back to the program to be used elsewhere
    return user_rectangle

def find_largest_rectangle(rectangle_list):
    # Assume the first rectangle is the largest initially
    largest = rectangle_list[0]
    max_area = largest.calc_area()

    # For each rectangle in the list
    for rectangle in rectangle_list:
        # Calculate the area of the current rectangle
        current_area = rectangle.calc_area()
        # If its area is bigger than the largest area we've seen
        if current_area > max_area:
            # Save this rectangle as the largest one
            largest = rectangle
            # Save its area as the largest area
            max_area = current_area

    # Return the largest rectangle we saw
    return largest


rectangles = []
# Create 5 rectangles
# This uses a function to create a rectangle for us
# We just save the result
for i in range(5):
    rect = create_rectangle()
    print(f"Rectangle created: {rect.display()}")
    rectangles.append(rect)

# Use a function to find the largest rectangle entered
largest = find_largest_rectangle(rectangles)
# Display that rectangle's information
largest.display()