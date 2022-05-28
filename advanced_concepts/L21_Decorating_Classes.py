import time 

def wait(s: int):
    def wait_deco(func):
        def wrapper(*args, **kwargs):
            print('Waiting {} seconds'.format(s))   
            time.sleep(s)
            func(*args, **kwargs)
        return wrapper
    return wait_deco

def greet(user):
    def wrapper(*args, **kwargs):
        value = user(*args, **kwargs)
        print('Hello, {}'.format(value.name))
        return value
    return wrapper


@greet
class User:

    def __init__(self, name: str):
        self.name = name
    
    @wait(3)
    def login(self) -> None:
        print(f'User {self.name} logged in')



user = User('Mario')
# user.login()