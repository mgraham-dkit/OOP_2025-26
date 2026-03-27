import json
from users import User


with open("user.json") as file:
    user_dict = json.load(file)

    u = User.from_dict(user_dict)

    print(f"User name: {u.name}")