import json
from tickets import Ticket


if __name__ == "__main__":
    filename = input("Please enter the json filename: ")
    with open(filename) as file:
        ticket_dicts = json.load(file)

        tickets = []
        for ticket_dict in ticket_dicts:
            ticket = Ticket.from_dict(ticket_dict)
            tickets.append(ticket)

        for i, ticket in enumerate(tickets):
            print(f"{i}: {repr(ticket)}")
