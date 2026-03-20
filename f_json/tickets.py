class Ticket:
    def __init__(self, ticket_id: int, title: str, desc: str, status: str, assigned_to: str):
        self.ticket_id = ticket_id
        self.title = title
        self.description = desc
        self.status = status
        self.assigned_to = assigned_to

    def __str__(self) -> str:
        return f"Ticket {self.ticket_id}: {self.title}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{ticket_id={self.ticket_id}, title={self.title}, description={self.description}, status={self.status}, assigned_to={self.assigned_to}}}"