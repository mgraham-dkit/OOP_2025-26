def multiply() -> None:
    try:
        num1 = float(input("Value one: "))
        num2 = float(input("Value two: "))

        print(f"{num1} * {num2} = {num1*num2}")
    except ValueError as e:
        print("Invalid input - please try again")

def add(num1: int | float, num2: int | float) -> int| float:
    return num1 + num2


keepRunning = True

while keepRunning:
    print("Choose from the following: ")
    print("1) Add two numbers")
    print("2) Multiply two numbers")
    print("exit to exit the calculate")
    choice = input()
    match(choice.lower()):
        case "1":
            pass
        case "2":
            multiply()
        case "exit":
            print("Goodbye!")
            keepRunning = False
            continue
        case _:
            print("Please enter a valid option from the menu")