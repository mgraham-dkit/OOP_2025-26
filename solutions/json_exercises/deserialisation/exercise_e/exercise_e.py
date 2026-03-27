import json
from addressed_users import User


with open("addressed_user.json") as file:
    user_dict = json.load(file)

    user1 = User.from_dict(user_dict)

    print(user1)