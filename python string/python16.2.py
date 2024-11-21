# finding frequency using  dict comprehension + operator+ split functions
import operator as op
string1 = "python is simple, python programming is easy, this is a python program"
print("original stringn is:" +str(string1))
string2 = string1.split()
result = {key: op.countOf(string2, key)for key in string2}
print("Word frequency is:" +str(result))