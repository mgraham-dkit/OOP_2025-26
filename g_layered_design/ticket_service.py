from tickets import Ticket
class TicketService:
    def __init__(self, assigned: dict[str, Ticket]):
        self.__assigned_tickets = dict.copy(assigned)

    def get_tickets_for_agent(self, agent: str):
        if agent.lower() not in self.__assigned_tickets:
            return None

        return  self.__assigned_tickets[agent.lower()]