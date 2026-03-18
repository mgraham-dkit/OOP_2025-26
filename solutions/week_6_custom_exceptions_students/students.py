from __future__ import annotations
from types import NotImplementedType


class InvalidIDError(Exception):
    pass


class InvalidGradeError(ValueError):
    pass


class Student:
    ID_PREFIX = "D00"

    def __init__(self, student_id: str, name: str):
        Student.__validate_id(student_id)
        self._student_id = student_id.upper()

        if not name:
            raise ValueError("Invalid name provided")
        self._name = name

        # No example or information to work from, so specify the type here for clarity
        self.__grades: dict[str, int|float] = {}

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented

        return self._student_id.upper() == other._student_id.upper()

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented

        return not self == other

    def __repr__(self) -> str:
        return f"Student{{_student_id={self._student_id}, name={self._name}, grades={self.__grades}}}"

    def __str__(self) -> str:
        return f"{self._student_id}: {self._name}"

    def get_student_id(self) -> str:
        return self._student_id

    @staticmethod
    def __validate_id(student_id: str) -> None:
        if not student_id:
            raise ValueError("No value provided for student ID")

        if not student_id.upper().startswith(Student.ID_PREFIX):
            raise InvalidIDError(f"Student ID does not start with {Student.ID_PREFIX}")

    @staticmethod
    def validate_grade(grade: int) -> None:
        if not grade:
            raise ValueError("No value provided for grade")

        if not isinstance(grade, int) and not isinstance(grade, float):
            raise InvalidGradeError("Non-numeric data provided for grade")

        if grade < 0 or grade > 100:
            raise InvalidGradeError(f"Grade supplied ({grade}) is outside allowable range for grades. Must be >=0 and <=100")

    def add_grade(self, subject: str, grade: int | float) -> bool:
        Student.validate_grade(grade)

        if subject.lower() in self.__grades:
            return False

        self.__grades[subject.lower()] = grade
        return True

    def get_grades(self) -> dict[str, int|float]:
        return self.__grades.copy()
