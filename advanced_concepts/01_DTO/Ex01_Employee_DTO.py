""" Employee -> first name, last name, email, mobile, reports_to """

class Employee:

    def __init__(self, first_name, last_name, email, mobile, reports_to):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.reports_to = reports_to
    
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, email: {self.email}, mobile: {self.mobile}, reports to: {self.reports_to}"
    
    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name and self.email == other.email:
            return True
        return False

if __name__ == "__main__":
    employee = Employee("John", "Doe", "jdoe1@company.com", "555-555-5555", "Boss Baby")
    employee2 = Employee("John", "Doe", "jdoe1@company.com", "555-555-5555", "Boss Baby")

    print(employee == employee2)
    print(employee)