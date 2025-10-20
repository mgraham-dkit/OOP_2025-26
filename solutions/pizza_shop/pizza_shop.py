from orders import Pizza


def get_nickname(user_order):
    valid_nickname = False
    new_nickname = None
    while not valid_nickname:
        new_nickname = input("Enter pizza nickname: ")
        if new_nickname not in user_order:
            valid_nickname = True
        else:
            print("That nickname is in use, please try again.")

    return new_nickname

def get_size():
    size = None

    valid_size = False
    while not valid_size:
        size = input("Enter pizza size: ")
        if Pizza.check_size(size):
            valid_size = True
        else:
            print("That size is invalid, please try again.")

    return size

def get_toppings():
    return ["tomato sauce", "cheese"]

def create_pizza():
    new_size = get_size()
    toppings = get_toppings()
    pizza = Pizza(toppings, new_size)

    return pizza

def display_order(order_data):
    print("---------------------------")
    for name, pizza in enumerate(order_data.items()):
        print(f"{name} pizza:")
        pizza.display()
        print(f"Cost: €{pizza.calc_price()}")
    print("---------------------------")


order = {}

username = input("Enter your username: ")

add_pizza = True
while add_pizza:
    choice = input("Do you wish to select a pizza? (Y/y for yes, any other key to close order)")
    if choice.lower() != "y":
        add_pizza = False
        continue

    nickname = get_nickname(order)
    new_pizza = create_pizza()
    new_pizza.display()
    order[nickname] = new_pizza

display_order(order)


