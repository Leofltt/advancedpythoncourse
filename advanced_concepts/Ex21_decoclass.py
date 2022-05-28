
def add_role(role):
    def decorator(cls):
        setattr(cls, 'role', role)
        return cls
    return decorator

@add_role('admin')
class User:

    def __init__(self, name: str):
        self.name = name
    
    def login(self) -> None:
        print(f'User {self.name} logged in')

user = User('Mario')
print(user.role)
