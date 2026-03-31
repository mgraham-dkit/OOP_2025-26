class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    @classmethod
    def from_dict(cls, data):
        if data["type"] != cls.__name__:
            raise ValueError(f"Invalid type value ({data["type"]}) within dict  - {cls.__name__} cannot deserialise")

        city = data["city"]
        street = data["street"]

        return cls(street, city)

    def to_dict(self) -> dict:
        address_dict = {}
        address_dict["type"] = self.__class__.__name__

        address_dict["street"] = self.street
        address_dict["city"] = self.city

        return address_dict

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    @classmethod
    def from_dict(cls, data):
        if data["type"] != cls.__name__:
            raise ValueError(f"Invalid type value ({data["type"]}) within dict  - {cls.__name__} cannot deserialise")

        address = Address.from_dict(data["address"])
        name = data["name"]

        return cls(name, address)

    def to_dict(self) -> dict:
        emp_dict = {}
        emp_dict["type"] = self.__class__.__name__

        emp_dict["name"] = self.name
        emp_dict["address"] = self.address.to_dict()

        return emp_dict