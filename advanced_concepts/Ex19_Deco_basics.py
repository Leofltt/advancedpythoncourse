from time import perf_counter

def print_time(func):
    def wrapper():
        start = perf_counter()
        func()
        end = perf_counter()
        print(f'Time taken: {end - start}')
    return wrapper

@print_time
def create_one_million_squares():
    return [i**2 for i in range(1000000)]
      

create_one_million_squares()