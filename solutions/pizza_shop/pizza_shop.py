from orders import Pizza


order = {}

username = input("Enter your username: ")
add_pizza = True

while add_pizza:
    choice = input("Do you wish to select a pizza? (Y/y for yes, any other key to close order)")
    if choice.lower() != "y":
        add_pizza = False
        continue

    valid_nickname = False
    while not valid_nickname:
        nickname = input("Enter pizza nickname: ")
        if nickname not in order:
            valid_nickname = True
        else:
            print("That nickname is in use, please try again.")

    valid_size = False
    while not valid_size:
        size = input("Enter pizza size: ")
        if Pizza.check_size(size):
            valid_size = True
        else:
            print("That size is invalid, please try again.")

    toppings = ["tomato sauce", "cheese"]

    pizza = Pizza(toppings, size)
    pizza.display()
    order[nickname] = pizza