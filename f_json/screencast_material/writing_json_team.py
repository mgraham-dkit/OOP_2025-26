from workers import Worker
from workers import Team
import json


def write_to_file(file_name: str, team: Team) -> None:
    team_dict = team.to_dict()
    with open(file_name, "w") as file:
        json.dump(team_dict, file, indent=4)


if __name__ == "__main__":
    worker1 = Worker("Helen", 53, ["python", "Java", "VB", "Javascript"])
    worker2 = Worker("Angelo", 23, ["marketing", "accounting", "HR"])
    worker3 = Worker("Katya", 37, ["typescript", "CSS", "Javascript"])

    team = Team("Mixed bag", [worker1, worker2, worker3])
    filename = "json_output/persisted_team.json"

    write_to_file(filename, team)