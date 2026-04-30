import logging

from tickets import Ticket
from ticket_persistence import TicketDataAccess

logger = logging.getLogger(__name__)

class TicketService:
    def __init__(self, ticket_data_access: TicketDataAccess = None):
        self._data_access = ticket_data_access

        self.__assigned_tickets = {}
        self.__unassigned_tickets = []

    def get_tickets_for_agent(self, agent: str) -> list[Ticket] | None:
        TicketService.validate_agent(agent)

        if agent.lower() not in self.__assigned_tickets:
            return None

        return  self.__assigned_tickets[agent.lower()]

    @staticmethod
    def validate_agent(agent: str):
        if not agent:
            raise ValueError("Agent name cannot be blank/None")

    def get_agents(self) -> list[str]:
        return list(self.__assigned_tickets.keys())

    def get_unassigned_tickets(self) -> list[Ticket]:
        return list(self.__unassigned_tickets)

    def _assign_ticket(self, agent: str, ticket: Ticket) -> None:
        TicketService.validate_agent(agent)

        # Link ticket to specified agent
        ticket.assign_to(agent)

        # Place ticket in list for assigned agent within the assigned dictionary
        # Get list for agent (default to empty list if there isn't one)
        agent_list = self.__assigned_tickets.setdefault(agent.lower(), [])
        # Adds ticket to agent's list
        agent_list.append(ticket)

        # Compliance logging - ticket stored and assigned
        logger.info(f"Assigned ticket to {agent} - ticket details: {ticket}")

    def assign_next_ticket(self, agent: str) -> bool:
        TicketService.validate_agent(agent)

        if len(self.__unassigned_tickets) == 0:
            return False

        # Get next ticket from the available list of unassigned tickets
        next_ticket = self.__unassigned_tickets[0]
        # Add to assigned dictionary
        self._assign_ticket(agent, next_ticket)
        # Remove from unassigned list - do this last in case something goes wrong along the way
        self.__unassigned_tickets.pop(0)
        return True
