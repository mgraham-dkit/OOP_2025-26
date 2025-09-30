from stock import StockItem

def get_prod_code(stock_item):
    return stock_item.prod_code

def display_stock_list(stock):
    print("Stock Items in system:")
    for s in stock:
        s.display()
        print(f"Profit: €{s.calc_profit()}")
    print("---------------------------")

def get_by_prod_code(stock_items, prod_code):
    for item in stock_items:
        if item.prod_code == prod_code:
            return item

    return None

def get_by_keyword(stock_items, keyword):
    matches = []
    for item in stock_items:
        if keyword in item.description:
            matches.append(item)

    return matches

def find_max_profit_item(stock_items):
    max_profit = 0
    max_item = stock_items[0]

    for item in stock_items:
        if item.calc_profit() > max_profit:
            max_profit = item.calc_profit()
            max_item = item

    return max_item



def create_stock_item():
    code = input("Product code: ")
    name = input("Product name: ")
    desc = input("Product description: ")
    cost = float(input("Cost price: "))
    sale = float(input("Sale price: "))
    quant = int(input("Quantity in stock: "))

    stock_unit = StockItem(code, name, cost, sale, quant, desc)

    return stock_unit


stock = []
for i in range(2):
    unit = create_stock_item()
    stock.append(unit)

display_stock_list(stock)

stock.sort(key=get_prod_code)

display_stock_list(stock)

code = input("Enter the code to be searched for: ")
match = get_by_prod_code(stock, code)
if match is not None:
    print("Match: ")
    match.display()
else:
    print("No match found")

keyword = input("Enter the keyword to be searched for: ")
matches = get_by_keyword(stock, keyword)
if len(matches) != 0:
    display_stock_list(stock)
else:
    print("No match found")