from tickets import Ticket
class TicketService:
    def __init__(self, assigned: dict[str, list[Ticket]] = None, unassigned: list[Ticket] = None):
        self.__assigned_tickets = dict.copy(assigned) if assigned else {}
        self.__unassigned_tickets = list.copy(unassigned) if unassigned else []

    def get_tickets_for_agent(self, agent: str):
        if agent.lower() not in self.__assigned_tickets:
            return None

        return  self.__assigned_tickets[agent.lower()]

    def get_agents(self):
        return list(self.__assigned_tickets.keys())