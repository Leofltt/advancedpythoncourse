def composer_generator():
    yield "Beethoven"
    yield "Bach"
    yield "Mozart"
    yield "Handel"
    yield "Schubert"

composr = composer_generator()

for c in composr:
    print(c)

def squares_sum(start,stop):
    i = start
    sum = 0
    while i < stop:
        sum += i ** 2
        yield sum 
        i += 1

print(list(squares_sum(0,5)))