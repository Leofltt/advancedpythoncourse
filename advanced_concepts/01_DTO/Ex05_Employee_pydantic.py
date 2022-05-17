""" Employee -> first name, last name, email, mobile, reports_to, full_name """

from __future__ import annotations
from typing import Union, Optional

from pydantic import BaseModel

class Employee(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile: str
    reports_to: Optional[Union[Employee,str]]
    full_name: str = None
    
    def __init__(__pydantic_self__, **data) -> None:
        super().__init__(**data)
        __pydantic_self__.full_name = f"{__pydantic_self__.first_name} {__pydantic_self__.last_name}"

if __name__ == "__main__":
    boss = Employee(first_name="Boss", last_name="Baby", email="iamtheboss@company.com", mobile="666-666-6666", reports_to="None")
    employee = Employee(first_name="John", last_name="Doe", email="jdoe1@company.com", mobile="555-555-5555", reports_to=boss)
    employee2 = Employee(first_name="John", last_name="Doe", email="jdoe1@company.com", mobile="555-555-5555", reports_to="Boss Baby")

    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@company.com",
        "mobile": 12345,
        "reports_to": "Boss Baby"
    }
    print(employee == employee2)
    print(employee)

    employee3 = Employee(**args_dict)
    print(employee3)
    print(employee3.full_name)