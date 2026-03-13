import logging

def configure_logging(logging_level: int) -> None:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Configure the logging set up and assign handlers
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging_level, handlers=[console_handler])

configure_logging(logging.DEBUG)
logger = logging.getLogger()

def multiply() -> None:
    valid = False
    while not valid:
        try:
            num1 = float(input("Value one: "))
            valid = True
        except ValueError as e:
            logger.info("Invalid input for value 1")
            print("Data invalid, please try again")

    valid = False
    while not valid:
        try:
            num2 = float(input("Value two: "))
            valid = True
        except ValueError as e:
            logger.info("Invalid input for value 2")
            print("Data invalid, please try again")


    print(f"{num1} * {num2} = {num1 * num2}")


def add(num1: int | float, num2: int | float) -> int| float:
    return num1 + num2


def display_menu():
    print("Choose from the following: ")
    print("1) Add two numbers")
    print("2) Multiply two numbers")
    print("exit to exit the calculate")


if __name__ == "__main__":
    keepRunning = True

    while keepRunning:
        display_menu()
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