from functools import reduce

def square(x):
    return x**2

numbers = [1,2,3,4,5]

# MAP

squared_numbers = map(square, numbers)

even_odd = map(lambda n: 'even' if n % 2 == 0 else 'odd', numbers)

# FILTER

evens = filter(lambda n: n % 2 == 0, numbers)

# REDUCE

sum_list = reduce(lambda x, y: x + y, numbers)
print(sum_list)