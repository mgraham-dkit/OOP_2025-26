import json
from users import User


with open("users.json") as file:
    users_dict_list = json.load(file)

    users = {}
    for user_dict in users_dict_list:
        u = User.from_dict(user_dict)
        users[u.name] = u

    print(users)