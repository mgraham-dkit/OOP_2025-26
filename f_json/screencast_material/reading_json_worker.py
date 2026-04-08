import json
import logging
from logging import config
from typing import Any

from workers import Worker

def configure_logging() -> None:
    with open("logging_config.json") as f:
        json_config = json.load(f)

    logging.config.dictConfig(json_config)

configure_logging()
logger = logging.getLogger(__name__)


def read_json(file_name: str) -> dict[str, Any]:
    with open(file_name) as file:
        single_worker_dict = json.load(file)
        return single_worker_dict


def display_dict_info(worker_dict: dict[str, Any]) -> None:
    print("Dict of information parsed from JSON file: ")
    for key, value in worker_dict.items():
        print(f"{key} : {value} (type: {type(value)})")
    print()


if __name__ == "__main__":
    filename = input("Please enter the json filename: ")
    try:
        worker_dict = read_json(filename)

        display_dict_info(worker_dict)

        print("Converting dict to Worker object: ")
        worker = Worker.from_dict(worker_dict)
        print(f"Worker details: {worker}")
        print(f"{repr(worker)}")
    except FileNotFoundError as e:
        print(f"File \"{filename}\" could not be found.")
        logger.error(f"Supplied json file (\"{filename}\") not found.")
    except ValueError as e:
        print("Malformed JSON - JSON object could not be correctly deserialised")
        logger.error(f"Error when parsing JSON from {filename}: {e}")