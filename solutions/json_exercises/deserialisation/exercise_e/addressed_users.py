class Address:
    def __init__(self, city):
        self.city = city

    @classmethod
    def from_dict(cls, data):
        return cls(data["city"])

    def __str__(self) -> str:
        return self.city

class User:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        address = Address.from_dict(data["address"])
        return cls(name, address)

    def __str__(self) -> str:
        return f"{self.name} lives in {self.address}"
