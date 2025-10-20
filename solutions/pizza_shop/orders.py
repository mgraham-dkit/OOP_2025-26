class Pizza:
    #_allowable_sizes = ["small", "medium", "large", "extra-large"]
    _SIZE_PRICE_INDEX = {
        "small" : 10,
        "medium" : 12,
        "large" : 15,
        "extra-large" : 18
    }
    _STANDARD_SIZE = "medium"
    _TOPPING_COST = 0.85

    def __init__(self, toppings, size="medium"):
        self.toppings = toppings
        if size.lower() in Pizza._SIZE_PRICE_INDEX:
            self._size = size.lower()
        else:
            self._size = Pizza._STANDARD_SIZE

    def display(self):
        toppings = ", ".join(self.toppings)
        print(f"{self._size} pizza with {toppings} toppings")

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if new_size.lower() in Pizza._SIZE_PRICE_INDEX:
            self._size = new_size.lower()
            return True
        else:
            return False

    @staticmethod
    def get_allowable_sizes():
        return list(Pizza._SIZE_PRICE_INDEX.keys())

    @staticmethod
    def check_size(size):
        if size.lower() in Pizza._SIZE_PRICE_INDEX:
            return True
        else:
            return False

    def calc_price(self):
        base_price = Pizza._SIZE_PRICE_INDEX[self._size]
        topping_price = len(self.toppings) * Pizza._TOPPING_COST

        return base_price + topping_price