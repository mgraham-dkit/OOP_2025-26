from g_layered_design.ticket_persistence import TicketDataAccess
from tickets import Ticket
from tickets import FeatureRequest
from tickets import TicketException
import logging
import logging.config
import json
from ticket_service import TicketService

def configure_logging_json() -> None:
    with open("logging_config.json") as f:
        config = json.load(f)

    logging.config.dictConfig(config)

configure_logging_json()
logger = logging.getLogger(__name__)


def load_ticket_model() -> TicketService | None:
    # Read file:
    filename = ""
    try:
        filename = input("Please enter ticket data filename: ")
        ticket_dao = TicketDataAccess()
        unassigned, assigned = ticket_dao.read_file(filename)
        ticket_service = TicketService(assigned, unassigned)
        return ticket_service
    except FileNotFoundError as e:
        logger.warning(f"Cannot open file {filename}")
        print(f"File {filename} cannot be found. Please enter a new filename.")
        return None


def display_ticket_list(ticket_service: TicketService) -> None:
    ticket_list = ticket_service.get_unassigned_tickets()
    if len(ticket_list) == 0:
        print("No unassigned tickets found")
        return

    print("Unassigned tickets: ")
    for i, ticket in enumerate(ticket_list, 1):
        print(f"{i}) {ticket}")
        logger.info(f"Ticket details viewed: {ticket}")


def display_agents(ticket_service: TicketService) -> None:
    agents = ticket_service.get_agents()
    if not agents:
        print("No agents currently registered to Tickets")
    else:
        for i, agent in enumerate(agents, start=1):
            print(f"{i}) {agent}")


def display_tickets_for_agent(ticket_service: TicketService) -> None:
    agent = input("Please enter agent name: ")
    agent_tickets = ticket_service.get_tickets_for_agent(agent)
    if not agent_tickets:
        print("No agent matching supplied name registered in system")
    else:
        for i, ticket in enumerate(agent_tickets, 1):
            print(f"{i}) {ticket}")
            logger.info(f"Ticket details viewed: {ticket}")


def assign_next_ticket(ticket_service: TicketService) -> None:
    agent = input("Enter agent name to assign next ticket: ")
    try:
        assigned = ticket_service.assign_next_ticket(agent)
        if not assigned:
            logger.info(f"No tickets currently available - could not assign to {agent}")
            print("No unassigned tickets available")
    except TicketException as e:
        logger.error(f"Attempting to assign previously assigned ticket: {e}")
        print(f"Cannot assign ticket - ticket is already assigned")
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


def run_ui(ticket_service: TicketService):
    # Run main application logic
    keep_running = True
    while keep_running:
        print("=" * 20)
        display_menu()
        choice = input()
        match choice.lower():
            case "1":
                display_agents(ticket_service)
            case "2":
                display_tickets_for_agent(ticket_service)
            case "3":
                display_ticket_list(ticket_service)
            case "4":
                assign_next_ticket(ticket_service)
            case "exit":
                keep_running = False
            case _:
                print("Invalid option selected")


if __name__ == "__main__":
    valid = False
    ticket_service = None
    while not valid:
        ticket_service = load_ticket_model()
        if ticket_service:
            valid = True

    run_ui(ticket_service)
