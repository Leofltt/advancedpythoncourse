from math import sqrt

ex02 = [sqrt(x) if x % 3 == 0 else x**2 for x in range(20)]

ex03 = [[i*j for i in range(3)] for j in range(4)]

print(ex03)