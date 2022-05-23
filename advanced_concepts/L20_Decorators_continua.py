import time

def greetings(func):
    def wrapper(*args, **kwargs):
        print('Hi')
        func(*args, **kwargs)
        print('Have a good day!')
        return args[0]
    return wrapper

@greetings
def hi_deco(name):
    print('Hello there, {}'.format(name))

nome = hi_deco("Mario")
print(nome)

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print('Execution time: {}'.format(end - start))
        return result
    return wrapper

@timing
def squares(stop_number):
    return [i**2 for i in range(stop_number)]

l_squares = squares(1000000)
print(l_squares[:10])

def wait(s: int):
    def wait_deco(func):
        def wrapper(*args, **kwargs):
            print('Waiting {} seconds'.format(s))   
            time.sleep(s)
            func(*args, **kwargs)
        return wrapper
    return wait_deco

@wait(3)
@timing
def hello(name: str):
    print('Hello, {}'.format(name))

hello('Mario')