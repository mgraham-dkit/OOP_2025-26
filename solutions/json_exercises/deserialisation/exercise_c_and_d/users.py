class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        age = data["age"]
        return cls(name, age)
