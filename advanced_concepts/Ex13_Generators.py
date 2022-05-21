import math 

def factorial_generator(start,stop):
    i = start
    while i < stop:
        n = math.factorial(i)
        yield n
        i += 1

print(list(factorial_generator(0,5)))

