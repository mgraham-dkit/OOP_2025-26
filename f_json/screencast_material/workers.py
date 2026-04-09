import logging
from typing import Any, Self
from types import NotImplementedType

logger = logging.getLogger(__name__)

class Worker:
    def __init__(self, name: str, age: int, skills:list[str] = None):
        self._name = Worker.validate_name(name)
        self._age = Worker.validate_age(age)
        self._skills = Worker.validate_skills(skills)

    # Validator methods
    @staticmethod
    def validate_name(name: str) -> str:
        if not name:
            raise ValueError("Name cannot be blank/None")

        return name

    @staticmethod
    def validate_age(age: int) -> int:
        if not age:
            raise ValueError("Age cannot be blank/None")

        if not isinstance(age, int):
            raise TypeError("Age must be an int")

        if age < 18:
            raise ValueError(f"Workers must be over 18 (age provided: {age}")

        return age

    @staticmethod
    def validate_skills(skills: list[str]) -> list[str]:
        # No/empty skill list provided, return empty list to be stored
        if not skills:
            return []

        validated_skills = []
        # Validate each skill supplied in parameter list
        for skill in skills:
            if not skill:
                logger.info("Ignoring blank skill")
            else:
                # Store validated skill (excluding leading and trailing whitespace)
                # converted to lowercase
                validated_skills.append(skill.strip().lower())

        return validated_skills

    # Identity methods
    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Worker):
            return NotImplemented

        return self._name.lower() == other._name.lower() and self._age == other._age

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Worker):
            return NotImplemented

        return not self == other

    # Text representation methods
    def __str__(self) -> str:
        return f"{self._name} is {self._age}. Skills include: {self._skills}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{_name={self._name}, _age={self._age}, _skills={self._skills}}}"

    # Serialisation methods
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        try:
            if data["type"] != cls.__name__:
                raise ValueError(
                    f"Invalid type value ({data["type"]}) within dict  - {cls.__name__} cannot deserialise")

            name = data["name"]
            age = data["age"]
            skills = data["skills"]
            return cls(name, age, skills)
        except KeyError as e:
            raise ValueError(f"JSON error occurred when building {cls.__name__} - cannot find key {e}")

    def to_dict(self) -> dict[str, str | int | list[str]]:
        data = {}

        data["type"] = self.__class__.__name__
        data["name"] = self._name
        data["age"] = self._age
        data["skills"] = self._skills

        return data


class Team:
    def __init__(self, name: str, members: list[Worker] = None):
        self._name = Team.validate_name(name)
        self._members = Team.validate_members(members)

    # Validator methods
    @staticmethod
    def validate_name(name: str) -> str:
        if not name:
            raise ValueError("Name cannot be blank/None")

        return name

    @staticmethod
    def validate_members(members: list[Worker]) -> list[Worker]:
        # No/empty member list provided, return empty list to be stored
        if not members:
            return []

        valid_members = []
        # Validate each member supplied in parameter list
        for member in members:
            if not member:
                logger.info("Ignoring blank member")
            elif member in valid_members:
                # Skip member if it's already in the list
                logger.info(f"Ignoring duplicate member: {member}")
            else:
                valid_members.append(member)
        return valid_members

    # Identity methods
    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Team):
            return NotImplemented

        return self._name.lower() == other._name.lower()

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Team):
            return NotImplemented

        return not self == other

    # Text representation methods
    def __str__(self) -> str:
        return f"{self._name} contains {len(self._members)} members."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{_name={self._name}, _members={self._members}}}"

    # Serialisation methods
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        try:
            if data["type"] != cls.__name__:
                raise ValueError(
                    f"Invalid type value ({data["type"]}) within dict  - {cls.__name__} cannot deserialise")

            name = data["name"]
            members = [Worker.from_dict(worker_dict) for worker_dict in data["members"]]
            return cls(name, members)
        except KeyError as e:
            raise ValueError(f"JSON error occurred when building {cls.__name__} - cannot find key {e}")

    def to_dict(self) -> dict[str, str | list[dict[str, str | int | list[str]]]]:
        data = {}

        data["type"] = self.__class__.__name__
        data["name"] = self._name

        data["members"] = [member.to_dict() for member in self._members]

        # List comprehension on line 169 is equivalent to the following:
        # member_dict_list = []
        # for member in self._members:
        #     member_dict = member.to_dict()
        #     member_dict_list.append(member_dict)
        #
        # data["members"] = member_dict_list

        return data
