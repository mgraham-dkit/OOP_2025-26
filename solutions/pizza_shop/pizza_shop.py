from datetime import datetime

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
    for name, pizza in order_data.items():
        print(f"{name} pizza:")
        pizza.display()
        print(f"Cost: €{pizza.calc_price()}")
    print("---------------------------")

def get_most_expensive(order_data):
    if not order_data:
        return None

    max = list(order_data.items())[0]
    max_nickname = max[0]
    max_pizza = max[1]
    max_price = max_pizza.calc_price()

    for nickname, pizza in order_data.items():
        current_price = pizza.calc_price()
        if current_price > max_price:
            max_pizza = pizza
            max_price = current_price
            max_nickname = nickname

    return max_nickname, max_pizza

def calc_total_cost(order_data):
    total_cost = 0
    for pizza in order_data.values():
        total_cost += pizza.calc_price()

    return total_cost

def save_order(order_dict, username):
    timestamp = datetime.now()
    text_timestamp = f"{timestamp.day}-{timestamp.month}-{timestamp.year}"
    file_name = f"{username}_{text_timestamp}.txt"
    #file_name = "michelle.txt"
    with open(file_name, 'w') as writer:
        for nick, pizza in order_dict.items():
            writer.write(f"{nick}: {pizza}\n")



order = {}

username = input("Enter your username: ")

hard_coded_pizza = Pizza(["ham", "pineapple", "marshmallow fluff"], "large")
order["default"] = hard_coded_pizza
pizza_list = [hard_coded_pizza]

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
result = get_most_expensive(order)
if result is not None:
    expensive_nickname, most_expensive_pizza = result
    print(f"Most expensive pizza in your order: {expensive_nickname} costing {most_expensive_pizza.calc_price()}")
    print("Details: ")
    most_expensive_pizza.display()
else:
    print("No pizzas were ordered")

total_price = calc_total_cost(order)
print(f"Your total is: €{total_price}")

save_order(order, username)