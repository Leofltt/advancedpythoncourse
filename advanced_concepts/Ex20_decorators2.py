def check_int(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError('Stop number must be greater than zero')
        value = func(*args, **kwargs)
        return value
    return wrapper

@check_int
def create_squares_list(stop: int):
   return [n**2 for n in range(stop)]

def filter_divisible_by(n: int):
    def filter_deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return [i for i in result if i % n == 0]
        return wrapper
    return filter_deco

@filter_divisible_by(2)
def create_squares_list_2(stop: int):
   return [n**2 for n in range(stop)]

print(create_squares_list_2(10))