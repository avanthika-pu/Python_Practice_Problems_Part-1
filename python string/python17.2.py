#conversion of snake case to pascal case using title(), split(), join()
string1 = "Python_Is_Simple"
print("Original string is:" +str(string1))
x = string1.split("_")
result = []
for i in x:
    i = i.title()
    result.append(i)
result = "".join(result)
print("After conversion :" +str(result))