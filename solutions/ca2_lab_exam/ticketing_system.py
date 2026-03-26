from typing import Any

from solutions.ca2_lab_exam.tickets import FeatureRequest, Ticket
from tickets import Ticket
from tickets import FeatureRequest
from tickets import TicketException
import logging
import logging.config
import json


def configure_logging_json() -> None:
    with open("logging_config.json") as f:
        config = json.load(f)

    logging.config.dictConfig(config)

configure_logging_json()
logger = logging.getLogger(__name__)


def parse_ticket(text: str) -> Ticket | None:
    line = text.strip().split("%%")
    # Line formats:
    # TICKET%%id%%title%%desc%%status%%assigned_to
    # FEATURE%%id%%title%%desc%%status%%assigned_to%requested%%approval%%status

    try:
        ticket_type = line[0]

        try:
            ticket_id = int(line[1])
        except ValueError as e:
            logger.error(f"Ticket id ({line[1]}) is in incorrect format - must be an int")
            print(f"Record is malformed [invalid ticket id] - skipping: {text}")
            return None

        title= line[2]
        desc = line[3]
        status = line[4]
        assigned_to = line[5]

        if ticket_type.upper() == "TICKET":
            ticket = build_ticket(assigned_to, desc, status, ticket_id, title)
            return ticket
        else:
            requested_feat = line[6]
            approval_status = line[7]

            feature_ticket = build_feature_request(approval_status, assigned_to, desc, text, requested_feat, status,
                                           ticket_id, title)
            return feature_ticket

    except IndexError as e:
        logger.warning(f"Malformed line - insufficient components provided. Line: {text}")
        print(f"Record is malformed [missing components] - skipping: {text}")
        return None
    except TicketException as e:
        logger.error(f"Issue with ticket data: {e} - skipping record: {text}")
        print(f"Issue with ticket data - skipping record: {text}")
        return None
    except ValueError as e:
        logger.warning(f"Missing information in line {text} - {e}")
        print(f"Record is malformed [missing components] - skipping: {text}")
        return None


def build_feature_request(approval_status: str, assigned_to: str, desc: str, line: str, requested_feat: str,
                          status: str, ticket_id: int, title: str) -> FeatureRequest:
    ticket = FeatureRequest(ticket_id, title, desc, requested_feat)
    ticket.update_status(status)
    ticket.assign_to(assigned_to)
    match approval_status.upper():
        case "APPROVED":
            ticket.approve()
        case "REJECTED":
            ticket.reject()
        case "PENDING":
            pass
        case _:
            raise TicketException(f"Illegal approval status ({approval_status}) supplied - skipping record: {line}")
    return ticket


def build_ticket(assigned_to: str, desc: str, status: str, ticket_id: int, title: str):
    ticket = Ticket(ticket_id, title, desc)
    ticket.update_status(status)
    if assigned_to != "":
        ticket.assign_to(assigned_to)
    return ticket


def read_file(filename: str) -> tuple[list[Ticket], dict[str, list[Ticket]]]:
    unassigned_tickets = []
    assigned_tickets = {}

    # Read file
    with open(filename) as file:
        for line in file:
            ticket = parse_ticket(line)
            if ticket is None:
                continue
            # If ticket is not assigned, place in list of unassigned tickets
            assigned_agent = ticket.get_assigned_agent()
            if assigned_agent == "":
                unassigned_tickets.append(ticket)
                # Compliance logging - ticket stored
                logger.info(f"Unassigned ticket added to queue: {ticket}")
            else:
                assign_ticket(assigned_agent, assigned_tickets, ticket)

    return unassigned_tickets, assigned_tickets


def assign_ticket(assigned_agent: str, assigned_tickets: dict[str, list[Ticket]], ticket: Ticket):
    # Otherwise, place in dictionary, associated with assigned agent
    agent_list = assigned_tickets.get(assigned_agent.lower(), [])
    agent_list.append(ticket)
    assigned_tickets[assigned_agent.lower()] = agent_list
    # Compliance logging - ticket stored and assigned
    logger.info(f"Assigned ticket to {assigned_agent} - ticket details: {ticket}")


def display_ticket_list(ticket_list: list[Ticket]) -> None:
    if len(ticket_list) == 0:
        print("No tickets found")
        return

    for i, ticket in enumerate(ticket_list, 1):
        print(f"{i}) {ticket}")
        logger.info(f"Ticket details viewed: {ticket}")


def display_agents(assigned_tickets: dict[str, list[Ticket]]) -> None:
    for i, agent in enumerate(assigned_tickets, start=1):
        print(f"{i}) {agent}")


def display_tickets_for_agent(assigned_tickets: dict[str, list[Ticket]]) -> None:
    agent = input("Please enter agent name: ")
    if agent.lower() not in assigned_tickets:
        print("No agent matching supplied name registered in system")

    agent_tickets = assigned_tickets[agent]
    for i, ticket in enumerate(agent_tickets, 1):
        print(f"{i}) {ticket}")
        logger.info(f"Ticket details viewed: {ticket}")


def assign_next_ticket(unassigned_list: list[Ticket], assigned_dict: dict[str, list[Ticket]]) -> None:
    if len(unassigned_list) == 0:
        logger.info("No tickets available to be assigned")
        return

    next_ticket = unassigned_list[0]
    print(f"Ticket to be assigned: {next_ticket}")

    agent = ""
    try:
        agent = input("Please enter agent name to be assigned a ticket: ")
        # Link to specified agent
        next_ticket.assign_to(agent)
        # Add to assigned dictionary
        assign_ticket(agent, assigned_dict, next_ticket)
        # Remove from unassigned list - do this last in case something goes wrong along the way
        unassigned_list.pop(0)
    except TicketException as e:
        logger.error(f"Attempting to assign previously assigned ticket: {e}")
        print(f"Cannot assign ticket - ticket is already assigned to {next_ticket.get_assigned_agent()}")
    except ValueError as e:
        logger.error(f"Attempting to assign ticket to illegal agent value: {e}")
        print(f"Cannot assign ticket - agent \"{agent}\" is invalid. Please try again with a different agent")


def display_menu() -> None:
    print("Please choose from the following options: ")
    print("-"*30)
    print("1) View all agents")
    print("2) Display tickets for selected agent")
    print("3) Display unassigned tickets")
    print("4) Assign next ticket")
    print("exit) Exit the program")


if __name__ == "__main__":
    # Read file:
    unassigned, assigned = read_file("tickets.txt")
    print("Unassigned data:")
    for t in unassigned:
        print(t)

    # Run main application logic
    keep_running = True
    while keep_running:
        print("=" * 20)
        display_menu()
        choice = input()
        match choice.lower():
            case "1":
                display_agents(assigned)
            case "2":
                display_tickets_for_agent(assigned)
            case "3":
                print("Unassigned tickets: ")
                display_ticket_list(unassigned)
            case "4":
                assign_next_ticket(unassigned, assigned)
            case "exit":
                keep_running = False
            case _:
                print("Invalid option selected")
