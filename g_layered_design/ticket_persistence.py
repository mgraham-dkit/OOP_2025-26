import logging
import os.path
from abc import ABC, abstractmethod

from tickets import Ticket
from tickets import FeatureRequest
from tickets import TicketException


logger = logging.getLogger(__name__)


class ITicketDataAccess(ABC):
    @abstractmethod
    def load_tickets(self) -> tuple[list[Ticket], dict[str, list[Ticket]]]:
        pass

class BlankTicketDataAccess(ITicketDataAccess):
    def __init__(self, filename):
        pass

    def load_tickets(self) -> tuple[list[Ticket], dict[str, list[Ticket]]]:
        return [], {}


class TicketDataAccess(ITicketDataAccess):
    def __init__(self, filename: str):
        if not filename:
            raise ValueError("Cannot read from None/blank file")

        if not os.path.exists(filename):
            raise FileNotFoundError(f"No such file: {filename}")

        self._filename = filename

    def parse_ticket(self, text: str) -> Ticket | None:
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

            title = line[2]
            desc = line[3]
            status = line[4]
            assigned_to = line[5]

            if ticket_type.upper() == "TICKET":
                ticket = self.build_ticket(assigned_to, desc, status, ticket_id, title)
                return ticket
            else:
                requested_feat = line[6]
                approval_status = line[7]

                feature_ticket = self.build_feature_request(approval_status, assigned_to, desc, text, requested_feat, status,
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

    def build_feature_request(self, approval_status: str, assigned_to: str, desc: str, line: str, requested_feat: str,
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

    def build_ticket(self, assigned_to: str, desc: str, status: str, ticket_id: int, title: str) -> Ticket:
        ticket = Ticket(ticket_id, title, desc)
        ticket.update_status(status)
        if assigned_to != "":
            ticket.assign_to(assigned_to)
        return ticket

    def load_tickets(self) -> tuple[list[Ticket], dict[str, list[Ticket]]]:
        unassigned_tickets = []
        assigned_tickets = {}

        # Read file
        with open(self._filename) as file:
            for line in file:
                ticket = self.parse_ticket(line)
                if ticket is None:
                    continue
                # If ticket is not assigned, place in list of unassigned tickets
                assigned_agent = ticket.get_assigned_agent()
                if assigned_agent == "":
                    unassigned_tickets.append(ticket)
                    # Compliance logging - ticket stored
                    logger.info(f"Unassigned ticket retrieved from file and added to queue: {ticket}")
                else:
                    agent_list = assigned_tickets.setdefault(assigned_agent.lower(), [])
                    agent_list.append(ticket)
                    logger.info(
                        f"Assigned ticket retrieved from file and added to queue for {assigned_agent}: {ticket}")

        return unassigned_tickets, assigned_tickets