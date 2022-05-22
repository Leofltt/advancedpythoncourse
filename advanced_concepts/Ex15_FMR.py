from math import sqrt
from functools import reduce


ex01 = map(lambda x: x / 2, [2,4,16,80])

assert list(ex01) == [1,2,8,40]

ex02 = filter(lambda x: sqrt(x).is_integer(), [2,4,16,80])

assert list(ex02) == [4,16]

ex03 = reduce(lambda x, y: x*y, [1,2,3])

assert ex03 == 6