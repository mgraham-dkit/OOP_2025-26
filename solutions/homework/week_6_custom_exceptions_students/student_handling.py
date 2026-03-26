from students import Student
from students import InvalidIDError
from students import InvalidGradeError


def parse_student(line: str) -> Student:
    components = line.split(",")
    if len(components) != 4:
        raise ValueError(f"Malformed record on line: {line}")

    student_id = components[0].strip().upper()
    name = components[1].strip()
    student = Student(student_id, name)

    subject = components[2].strip()

    try:
        if "." in components[3].strip():
            grade = float(components[3].strip())
        else:
            grade = int(components[3].strip())
    except ValueError as e:
        raise InvalidGradeError("Non-numeric grade data supplied.")

    student.add_grade(subject, grade)
    return student


def parse_student_file(filename: str) -> dict[str, Student]:
    student_records = {}
    with open(filename) as file:
        for line_no, line in enumerate(file):
            try:
                line = line.strip()
                student = parse_student(line)

                if student.get_student_id() not in student_records:
                    student_records[student.get_student_id()] = student
                else:
                    # Retrieve grade dictionary of student parsed from current line
                    student_grades = student.get_grades()
                    # Retrieve existing version of student in overall record
                    existing_student = student_records[student.get_student_id()]
                    # Add grade from current line into existing student
                    for subject, grade in student_grades.items():
                        existing_student.add_grade(subject, grade)

            except InvalidIDError as e:
                print(f"InvalidIDError: Invalid student ID provided on line {line_no}")
                print(f"Error: {e.args[0]}")
            except InvalidGradeError as e:
                print(f"InvalidGradeError: Invalid grade provided on line {line_no}")
                print(f"Error: {e.args[0]}")
            except ValueError as e:
                print(f"An error occurred parsing line {line_no}")
                print(f"Error: {e.args[0]}")

    return student_records


def find_student(student_dict: dict[str, Student]) -> None:
    id_num = input("Please enter student id: ")
    target = student_dict.get(id_num)

    if not target:
        print(f"No student found matching supplied student ID ({id_num})")
    else:
        print(target)


def display_students(student_dict: dict[str, Student]) -> None:
    for student in student_dict.values():
        print(f"{student}. Grades: {student.get_grades()}")


if __name__ == "__main__":
    filename = input("Please enter filename for student data file: ")
    try:
        students = parse_student_file(filename)
        display_students(students)
        find_student(students)
    except FileNotFoundError as e:
        print(f"File ({filename}) could not be found.")
    print("Program terminating...")