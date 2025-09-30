from stock import StockItem

def get_prod_code(stock_item):
    return stock_item.prod_code


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

for s in stock:
    s.display()
    print(f"Profit: €{s.calc_profit()}")


stock.sort(key=get_prod_code)
for s in stock:
    s.display()