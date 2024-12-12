# converting snake case to pascal case using title() and replace()
string1 = "python_is_simple"
print("original string is:" +str(string1))
result = string1.replace("_","").title().replace(" ","")
print("After conversion :" +str(result))
print(result)