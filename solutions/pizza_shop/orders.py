class Pizza:
    _allowable_sizes = ["small", "medium", "large", "extra-large"]

    def __init__(self, toppings, size="medium"):
        self.toppings = toppings
        if size.lower() in Pizza._allowable_sizes:
            self._size = size.lower()
        else:
            self._size = Pizza._allowable_sizes[1]

    def display(self):
        toppings = ", ".join(self.toppings)
        print(f"{self._size} pizza with {toppings} toppings")

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if new_size.lower() in Pizza._allowable_sizes:
            self._size = new_size.lower()
            return True
        else:
            return False

    @staticmethod
    def get_allowable_sizes():
        return list(Pizza._allowable_sizes)

    @staticmethod
    def check_size(size):
        if size.lower() in Pizza._allowable_sizes:
            return True
        else:
            return False
