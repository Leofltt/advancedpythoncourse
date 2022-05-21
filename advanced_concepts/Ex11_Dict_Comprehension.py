from math import pow

dict_1 = {f'power_{powr}': [pow(n, powr) for n in range(5)] for powr in range(4)}
print(dict_1)

sample_dict = {'a': 1, 'b': 4, 'c': 17,'d': 16}  

solution = {k:v for (k,v) in sample_dict.items() if v % 4 == 0}
print(solution)