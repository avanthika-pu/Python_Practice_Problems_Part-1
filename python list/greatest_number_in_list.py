# finding greatest number using reduce method
from functools import reduce
a = [10, 20, 30, 40]
largest_element = reduce(lambda x, y: x if x > y else y, a)
print(largest_element)