class Product:
    # As Product has a specific prefix attached to every ID, we need to encode that here
    __ID_PREFIX = "PROD_"

    # As there is no way to halt creation, we need default values to fall back to
    __DEFAULT_ID_VALUE = "Default ID - CHANGE IMMEDIATELY"
    __DEFAULT_UNIT_PRICE = 3
    __DEFAULT_UNITS_IN_STOCK = 0

    def __init__(self, prod_id: str, name: str, unit_price: float, units_in_stock: int):
        """ Creates an instance of Product containing specified values.
        If values do not meet requirements, default values are inserted.
        Defaults are specified by class attributes.

        Args:
            prod_id: The id of the new product (ID should begin with __ID_PREFIX)
            name: The name of the new product (name may be blank)
            unit_price: Price per unit for this product (must be greater than 0)
            units_in_stock: Number of units currently in stock for this product (cannot be less than 0)
        """
        # Product ID must start with specific start sequence - need to validate before storing
        if Product.validate_id(prod_id):
            # Convert id to uppercase
            prod_id = prod_id.upper()
            self._prod_id = prod_id
        else:
            self._prod_id = Product.__DEFAULT_ID_VALUE

        # No logic for name structure - no need to validate
        self.name = name

        # Price cannot be below 0 - need to validate before storing
        if Product.validate_price(unit_price):
            self._unit_price = unit_price
        else:
            self._unit_price = Product.__DEFAULT_UNIT_PRICE

        # Number of units in stock cannot be below 0 - need to validate before storing
        if Product.validate_units(units_in_stock):
            self._units_in_stock = units_in_stock
        else:
            self._units_in_stock = Product.__DEFAULT_UNITS_IN_STOCK

    # Getter methods
    @staticmethod
    def get_default_id():
        return Product.__DEFAULT_ID_VALUE

    @staticmethod
    def get_prefix():
        return Product.__ID_PREFIX

    # Validators
    @staticmethod
    def validate_id(prod_id: str) -> bool:
        """ Validates a product ID to confirm it starts with appropriate prefix (case-insensitive).
        Prefix is specified by __ID_PREFIX.

        Args:
            prod_id: The product ID to be validated

        Returns:
            True if the product ID starts with the appropriate prefix; False otherwise.
        """

        # Check for real data - does product id exist
        if prod_id is None:
            print("Product ID cannot be None")
            return False

        # Check for good data - is product id suitable based on our requirements (starts with specified prefix - case-insensitive)
        if not prod_id.upper().startswith(Product.__ID_PREFIX):
            print(f"Invalid product ID supplied - ID must begin with {Product.__ID_PREFIX}")
            return False

        # Passes all requirements, return True
        return True

    @staticmethod
    def validate_price(price: float) -> bool:
        """ Validates a unit price to confirm it exists and is greater than 0.

        Args:
            price: The unit price to be validated

        Returns:
            True if the unit price exists and is greater than 0; False otherwise.
        """
        # Check for real data - does price exist
        if price is None:
            print("Price cannot be None")
            return False

        # Check for good data - is price suitable based on our requirements (must be > 0)
        if price <= 0:
            print("Invalid unit price supplied - price must be greater than 0")
            return False

        # Passes all requirements, return True
        return True

    @staticmethod
    def validate_units(units: float) -> bool:
        """ Validates a unit quantity to confirm it exists and is greater than or equal to 0.

        Args:
            units: The quantity of units to be validated

        Returns:
            True if the quantity of units exists and is greater than or equal to 0; False otherwise.
        """
        # Check for real data - does price exist
        if units is None:
            print("Unit quantity cannot be None")
            return False

        # Check for good data - is units suitable based on our requirements (must be >= 0)
        if units < 0:
            print("Invalid unit quantity supplied - unit quantity must be greater than or equal to 0")
            return False

        # Passes all requirements, return True
        return True


class Order:
    # Order number
    # Username
    # Product id
    # Quantity
    # Price
    pass

if __name__ == "__main__":
    print("Creating valid product (no error messages should be displayed)")
    valid_prod = Product(f"{Product.get_prefix()}001", "Apples", 0.59, 300)
    print("-" * 30)

    # Test ID validation
    print("Creating product with bad ID (ID error should be displayed)")
    bad_ID_no_prefix = Product("002", "Oranges", 0.89, 200)
    print("-" * 30)

    print("Creating product with None for ID (None ID error should be displayed)")
    bad_ID_none = Product(None, "Peaches", 1.05, 150)
    print("-" * 30)

    # Test unit price validation
    print("Creating product with negative unit price (Negative unit price error should be displayed)")
    bad_price_negative_value = Product(f"{Product.get_prefix()}004", "Cherries", -12.50, 10)
    print("-" * 30)

    print("Creating product with unit price of 0 (0 unit price error should be displayed)")
    bad_price_zero_price = Product(f"{Product.get_prefix()}005", "Plums", 0, 20)
    print("-" * 30)

    print("Creating product with None for price (None unit price error should be displayed)")
    bad_price_none_price = Product(f"{Product.get_prefix()}006", "Pineapples", None, 40)
    print("-" * 30)

    # Test quantity validation
    print("Creating product with negative quantity (Negative quantity error should be displayed)")
    bad_quantity_negative_value = Product(f"{Product.get_prefix()}007", "Bananas", 0.79, -30)
    print("-" * 30)

    print("Creating product with None for quantity (None unit quantity error should be displayed)")
    bad_quantity_none_value = Product(f"{Product.get_prefix()}008", "Dragon fruit", 0.79, None)
    print("-" * 30)

    print("Creating product with quantity set to 0 (No error should be displayed)")
    valid_quantity_zero = Product(f"{Product.get_prefix()}009", "Strawberries", 2.89, 0)
    print("-" * 30)