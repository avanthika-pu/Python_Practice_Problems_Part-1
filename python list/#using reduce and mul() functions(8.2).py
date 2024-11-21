#using reduce and mul() functions
from functools import reduce
from operator import mul
a = [10,20,30,40]
result = reduce(mul,a)
print(result)