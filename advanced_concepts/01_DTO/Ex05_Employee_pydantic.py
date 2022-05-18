""" Employee -> first name, last name, email, mobile, reports_to, full_name """

from __future__ import annotations
from typing import Union, Optional, List, Dict, Any

from pydantic import BaseModel, validator

class EmailError(Exception):
    
    def __init__(self, email: str, message: str) -> None:
        self.email = email
        self.message = message

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
    
    @validator('email')
    @classmethod
    def check_email_is_valid(cls, value: str, values: Dict[str, Any]) -> None:
        name = values.get('first_name')
        surname = values.get('last_name')
        email_address = (name[0] + surname + "@company.com").lower()
        if value != email_address:
            raise EmailError(value, f"Email address {value} is not valid and should be {email_address}")
        return value

if __name__ == "__main__":
    boss = Employee(first_name="Boss", last_name="Baby", email="bbaby@company.com", mobile="666-666-6666", reports_to="None")
    employee = Employee(first_name="John", last_name="Doe", email="jdoe@company.com", mobile="555-555-5555", reports_to=boss)
    employee2 = Employee(first_name="John", last_name="Doe", email="jdoe@company.com", mobile="555-555-5555", reports_to="Boss Baby")

    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@company.com",
        "mobile": 12345,
        "reports_to": "Boss Baby"
    }
    # print(employee == employee2)
    # print(employee)

    employee3 = Employee(**args_dict)
    print(employee3)
    # print(employee3.full_name)