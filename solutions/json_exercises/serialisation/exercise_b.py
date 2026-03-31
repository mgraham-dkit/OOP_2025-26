import json
from users import User


user1 = User("Alpha", 30)
user2 = User("Beta", 21)
user3 = User("Omega", 99)

user_list = [user1, user2, user3]

json_users = [user.to_dict() for user in user_list]
# for user in user_list:
#     user_dict = user.to_dict()
#     json_users.append(user_dict)

with open("users.json", "w") as file:
    json.dump(json_users, file, indent=4)