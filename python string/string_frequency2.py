# finding frequency of a string using defaultdict
from collections import defaultdict
string1 = 'python is simple, python programming is simple, this is python'
print("original string is:" +str(string1))
string2 = string1.split()
frequency = defaultdict(int)
for word in string2:
    frequency[word] += 1
result = dict(frequency)
print(result)