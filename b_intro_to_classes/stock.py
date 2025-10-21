from statistics import quantiles


class StockItem:
    def __init__(self, prod_code, name, cost_price, sale_price, quantity, description="Default description"):
        self.prod_code = prod_code
        self.name = name
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.quantity = quantity
        self.description = description

    def display(self):
        print(f"{self.prod_code}: {self.name} = €{self.cost_price} (cost)")

    def calc_profit(self):
        return (self.sale_price - self.cost_price) * self.quantity


class PerishableStockItem(StockItem):
    def __init__(self, prod_code, name, expiry, origin, cost_price, sale_price, quantity, description="Default description"):
        super().__init__(prod_code, name, cost_price, sale_price, quantity, description)
        self.expiry = expiry
        self.origin = origin

    def display(self):
        print(f"{self.prod_code}: {self.name} = €{self.cost_price} (cost) [Expires: {self.expiry}")
