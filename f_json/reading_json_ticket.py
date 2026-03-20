import json



if __name__ == "__main__":
    filename = input("Please enter the json filename: ")
    with open(filename) as file:
        ticket_dict = json.load(file)

        for key, value in ticket_dict.items():
            print(f"{key} : {value}")

        # if ticket_dict["assigned_to"] == "Jason":
        #     print("Jason is assigned to this ticket")
        # else:
        #     print("This is not Jason's record")
        #


