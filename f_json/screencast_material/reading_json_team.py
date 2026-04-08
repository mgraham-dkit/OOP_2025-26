import json
import logging
from logging import config
from typing import Any

from workers import Team

def configure_logging() -> None:
    with open("logging_config.json") as f:
        json_config = json.load(f)

    logging.config.dictConfig(json_config)

configure_logging()
logger = logging.getLogger(__name__)


def read_json(file_name: str) -> dict[str, Any]:
    with open(file_name) as file:
        team_dict = json.load(file)
        return team_dict


if __name__ == "__main__":
    filename = input("Please enter the json filename: ")
    try:
        team_dict = read_json(filename)

        print("Converting dict to Team object: ")
        team = Team.from_dict(team_dict)
        print(f"Team details: {team}")
        print(f"{repr(team)}")
    except FileNotFoundError as e:
        print(f"File \"{filename}\" could not be found.")
        logger.error(f"Supplied json file (\"{filename}\") not found.")
    except ValueError as e:
        print("Malformed JSON - JSON object could not be correctly deserialised")
        logger.error(f"Error when parsing JSON from {filename}: {e}")