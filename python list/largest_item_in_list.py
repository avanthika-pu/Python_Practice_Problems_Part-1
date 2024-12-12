from functools import reduce
a = [10, 20, 30, 40]
largest = reduce(lambda x, y: x if x > y else y, a)
print(largest)