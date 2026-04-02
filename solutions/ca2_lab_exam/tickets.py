from __future__ import annotations
from types import NotImplementedType


class TicketException(ValueError):
    pass


class Ticket:
    __STATUS_OPTIONS = ["OPEN", "IN_PROGRESS", "RESOLVED", "CLOSED"]

    def __init__(self, ticket_id: int, title: str, desc: str):
        # Validate supplied data
        self._ticket_id = Ticket.validate_id(ticket_id)
        self._title = Ticket.validate_string(title, "Title")
        self._description = Ticket.validate_string(desc, "Description")

        # Set default data
        self.__status = Ticket.__STATUS_OPTIONS[0]
        self._assigned_to = ""

    @staticmethod
    def validate_id(id_val: int) -> int:
        if not id_val:
            raise ValueError(f"Id cannot be blank")

        if not isinstance(id_val, int):
            raise TicketException(f"Id ({id_val}) must be supplied as an integer")

        if id_val <= 0:
            raise TicketException(f"Id number ({id_val}) must be greater than 0")

        return id_val

    @staticmethod
    def validate_string(field: str, field_name: str) -> str:
        if not field:
            raise ValueError(f"{field_name} cannot be blank")

        return field

    # Text representation
    def __str__(self) -> str:
        if self._assigned_to:
            assigned_name = f"assigned to {self._assigned_to}"
        else:
            assigned_name = "- unassigned"

        return f"{self._ticket_id}: {self._title} {assigned_name} [{self.__status}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{_ticket_id={self._ticket_id}, _title={self._title}, _description={self._description}, __status={self.__status}, _assigned_to={self._assigned_to}}}"

    # Equality/identity
    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Ticket):
            return NotImplemented

        return self._ticket_id == other._ticket_id

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Ticket):
            return NotImplemented

        return not self == other

    # Rich comparison
    def __lt__(self, other: Ticket) -> bool | NotImplementedType:
        if not isinstance(other, Ticket):
            return NotImplemented

        return self._ticket_id < other._ticket_id

    def __le__(self, other: Ticket) -> bool | NotImplementedType:
        if not isinstance(other, Ticket):
            return NotImplemented

        return self._ticket_id <= other._ticket_id

    def __gt__(self, other: Ticket) -> bool | NotImplementedType:
        if not isinstance(other, Ticket):
            return NotImplemented

        return self._ticket_id > other._ticket_id

    def __ge__(self, other: Ticket) -> bool | NotImplementedType:
        if not isinstance(other, Ticket):
            return NotImplemented

        return self._ticket_id >= other._ticket_id

    # Getters
    def get_status(self) -> str:
        return self.__status

    def get_assigned_agent(self) -> str:
        return self._assigned_to

    # Update actions
    def assign_to(self, agent: str) -> None:
        agent = Ticket.validate_string(agent, "Assigned agent")

        if self._assigned_to != "":
            raise TicketException(f"Ticket is already assigned to {self._assigned_to} - cannot be reassigned to {agent}")

        self._assigned_to = agent

    def update_status(self, new_status: str) -> None:
        new_status = Ticket.validate_string(new_status, "Status")

        if new_status.upper() not in Ticket.__STATUS_OPTIONS:
            raise TicketException(f"Supplied status ({new_status}) is not a valid status option")

        self.__status = new_status


class FeatureRequest(Ticket):
    _PENDING_STATUS= "PENDING"
    _APPROVED_STATUS="APPROVED"
    _REJECTED_STATUS="REJECTED"

    def __init__(self, ticket_id: int, title: str, desc: str, requested_feature: str):
        super().__init__(ticket_id, title, desc)

        self._requested_feature = Ticket.validate_string(requested_feature, "Requested feature")
        self.__approval_status = FeatureRequest._PENDING_STATUS

    def __str__(self) -> str:
        return f"[FEATURE] {super().__str__()} -> {self._requested_feature}"

    def __repr__(self) -> str:
        text = super().__repr__()[:-1]
        return f"{text}, _requested_feature={self._requested_feature}, __approval_status={self.__approval_status}}}"

    def approve(self) -> None:
        self.__approval_status = FeatureRequest._APPROVED_STATUS
        self.update_status("CLOSED")

    def reject(self) -> None:
        self.__approval_status = FeatureRequest._REJECTED_STATUS
        self.update_status("CLOSED")

    def get_approval_status(self) -> str:
        return self.__approval_status