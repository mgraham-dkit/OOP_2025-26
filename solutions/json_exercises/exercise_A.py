import json

with open("exercise_a.json") as file:
    file_dict = json.load(file)

    print(f"Json returned {type(file_dict)}")

    print(f"Name: {file_dict["name"]}")
    skill_list = file_dict["skills"]
    print(f"Second skill: {skill_list[1]}")