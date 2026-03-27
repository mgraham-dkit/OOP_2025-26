import json
from addressed_users import User


with open("addressed_users.json") as file:
    user_dict_list = json.load(file)

    user_list = [User.from_dict(user_dict) for user_dict in user_dict_list]

    for user in user_list:
        print(user)