import logging

def configure_logging(logging_level: int) -> None:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    student_file_handler = logging.FileHandler(filename="logs/student_log.txt", mode="a")
    student_file_handler.setLevel(logging.WARNING)

    # Configure the logging set up and assign handlers
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging_level, handlers=[console_handler, student_file_handler])


# configure logging setup across the module
configure_logging(logging.DEBUG)
logger = logging.getLogger()

def display(data: list) -> None:
    print("Product details:")
    print(f"\tID: {data[0]}")
    print(f"\tName: {data[1]}")
    if len(data) == 7:
        print(f"\tAuthor: {data[5]}")
    print(f"\tCost price: {data[2]}")
    print(f"\tRetail price: {data[3]}")
    print(f"\tQuantity in stock: {data[4]}")
    if len(data) == 7:
        print(f"\tGenre(s): {data[6]}")


def parse_product(line_no: int, line: str) -> list:
    components = line.split("%%")
    data = [components[1], components[2]]
    try:
        data.append(float(components[3]))
    except ValueError as e:
        data.append(0)
        logger.warning(
            f"{e.__class__.__name__}: No/Invalid cost price supplied on line {line_no}. Adding default value of 0. Original line content: {line}")

    try:
        data.append(float(components[4]))
    except ValueError as e:
        data.append(0)
        logger.warning(
            f"{e.__class__.__name__}: No/Invalid retail price supplied on line {line_no}. Adding default value of 0. Original line content: {line}")

    try:
        data.append(int(components[5]))
    except ValueError as e:
        print("No/Invalid quantity information supplied. Adding default value of 0")
        data.append(0)
        logger.warning(
            f"{e.__class__.__name__}: No/Invalid quantity information supplied on line {line_no}. Adding default value of 0. Original line content: {line}")

    if components[0] == "Book":
        data.append(components[6])
        genres = components[7].split("&&")
        data.append(genres)

    return data


def read_file(filename: str) -> None:
    with open(filename, "r") as file_handle:
        # Read content of file in and store in a list of content
        for line_no, line in enumerate(file_handle):
            line = line.strip()
            try:
                data = parse_product(line_no, line)
                # Display data for this line
                display(data)
            except ValueError as e:
                print("Malformed line detected - inappropriate data provided - skipping line.")
                print(f"Problem line: {line}")
                logger.warning(f"Malformed line [inappropriate data] detected on line {line_no}: {line}")
            except IndexError as e:
                print("Malformed line detected - insufficient information, data missing from line - skipping line.")
                print(f"Problem line: {line}")
                logger.warning(f"Malformed line [insufficient information] detected on line {line_no}: {line}")



if __name__ == "__main__":
    # Ask user to enter a filename
    filename = input("Please enter the inventory filename: ")
    try:
        read_file(filename)

    except FileNotFoundError as e:
        print("Invalid/unavailable file provided. Program terminating...")
        print(f"Filename provided: {filename}")
        logger.error(f"File not found (filename: {filename})")