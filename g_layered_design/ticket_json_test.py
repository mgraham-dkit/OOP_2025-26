from g_layered_design.ticket_persistence import JsonTicketDataAccess

ticket_dao = JsonTicketDataAccess("tickets.json")
unassigned, assigned = ticket_dao.load_tickets()

print("Unassigned tickets:")
for i, ticket in enumerate(unassigned):
    print(f"{i}) {ticket}")

print("Assigned tickets:")
for agent, agent_tickets in assigned.items():
    print(f"Tickets assigned to {agent}")
    for i, ticket in enumerate(agent_tickets):
        print(f"{i}) {ticket}")