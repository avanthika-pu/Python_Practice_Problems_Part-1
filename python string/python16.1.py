# finding frequency of a string using counter() and split()
from collections import Counter
string1 = "python is simple, This is python program, python is a simple program,python programming very easy"
print("The original string is:" + str(string1))
result = Counter(string1.split())
print("The frequency is:" + str(dict(result)))
