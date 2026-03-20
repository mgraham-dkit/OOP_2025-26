import json
from tickets import Ticket


def to_ticket(ticket_dict_obj):
    try:
        ticket_id = ticket_dict_obj["ticket_id"]
        title = ticket_dict_obj["title"]
        desc = ticket_dict_obj["description"]
        status = ticket_dict_obj["status"]
        assigned = ticket_dict_obj["assigned_to"]
        return Ticket(ticket_id, title, desc, status, assigned)
    except KeyError as e:
        print(f"KeyError occurred on {e} in {ticket_dict_obj}")



if __name__ == "__main__":
    filename = input("Please enter the json filename: ")
    with open(filename) as file:
        ticket_dicts = json.load(file)

        tickets = []
        for ticket_dict in ticket_dicts:
            ticket = to_ticket(ticket_dict)
            tickets.append(ticket)

        for i, ticket in enumerate(tickets):
            print(f"{i}: {ticket}")
