from workers import Worker
import json


def write_to_file(file_name: str, worker: Worker) -> None:
    worker_dict = worker.to_dict()
    with open(file_name, "w") as file:
        json.dump(worker_dict, file, indent=4)


if __name__ == "__main__":
    worker1 = Worker("Helen", 53, ["python", "Java", "VB", "Javascript"])
    filename = "json_output/persisted_worker.json"

    write_to_file(filename, worker1)