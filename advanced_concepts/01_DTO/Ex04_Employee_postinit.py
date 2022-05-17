""" Employee -> first name, last name, email, mobile, reports_to, full_name """

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Union, Optional

@dataclass
class Employee:
    first_name: str
    last_name: str
    email: str
    mobile: str
    reports_to: Optional[Union[Employee,str]]
    full_name: str = field(init= False)

    @classmethod
    def from_dict(cls, data: dict) -> Employee:
        return cls(**data)
    
    def __post_init__(self) -> None:
        self.full_name = f"{self.first_name} {self.last_name}"

if __name__ == "__main__":
    boss = Employee("Boss", "Baby", "iamtheboss@company.com", "666-666-6666", "None")
    employee = Employee("John", "Doe", "jdoe1@company.com", "555-555-5555", boss)
    employee2 = Employee("John", "Doe", "jdoe1@company.com", "555-555-5555", "Boss Baby")

    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@company.com",
        "mobile": 12345,
        "reports_to": ["Boss Baby"]
    }
    print(employee == employee2)
    print(employee)

    employee3 = Employee.from_dict(args_dict)
    print(employee3)
    print(employee3.full_name)