# Entity representing a student
from datetime import date
from typing import Optional
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    dob: date
    grade: int
    gpa: Optional[float] = None
    id: Optional[int] = None

    # def __init__(self, name: str, dob: date, grade: int, gpa: float = None, id: int = None) -> None:
    #     self._id = id
    #     self._name = name
    #     self._dob = dob
    #     self._grade = grade
    #     self._gpa = gpa

    # def get_id(self):
    #     return self._id

    # def set_id(self, value: int):
    #     self._id = value

    # def get_name(self) -> str:
    #     return self._name

    # def set_name(self, value: str):
    #     self._name = value

    # def get_dob(self) -> date:
    #     return self._dob

    # def set_dob(self, value: date):
    #     self._dob = value

    # def get_grade(self) -> int:
    #     return self._grade

    # def set_grade(self, value: int):
    #     self._grade = value

    # def get_gpa(self) -> Optional[float]:
    #     return self._gpa

    # def set_gpa(self, value: float):
    #     self._gpa = value
