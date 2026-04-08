class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

    def to_dict(self) -> dict:
        user_dict = {}
        user_dict["type"] = self.__class__.__name__

        user_dict["name"] = self.name
        user_dict["age"] = self.age

        return user_dict
