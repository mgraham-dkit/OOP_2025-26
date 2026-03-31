import json
from users import User


user1 = User("Alpha", 30)
user2 = User("Beta", 21)
user3 = User("Omega", 99)

user_dict = user1.to_dict()
with open("user.json", "w") as file:
    json.dump(user_dict, file, indent=4)