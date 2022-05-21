squares = {0: 0, 1: 1, 2: 4, 3: 9}

sq_dc = {x: x**2 for x in range(4)}
print(sq_dc)

dictionary = {'a': 0, 'b': 2, 'c': 3}
sq_dictionary = {'a': 0, 'b': 4, 'c': 9}

sq_dc_2 = {k:v**2 for (k,v) in dictionary.items()}
print(sq_dc_2)

even_odd = {k: 'even' if v % 2 == 0 else 'odd' for (k,v) in dictionary.items()}
print(even_odd)