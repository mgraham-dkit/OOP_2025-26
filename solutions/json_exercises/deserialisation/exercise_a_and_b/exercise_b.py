import json

with open("exercise_b.json") as file:
    data_list = json.load(file)

    print(f"Json returned {type(data_list)}")

    for i, file_dict in enumerate(data_list, 0):
        print(f"{i}) {file_dict["name"]}")