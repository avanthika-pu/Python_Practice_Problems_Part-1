# converting snake case to pascal case using capword()
import string
string1 = "hai_you_doing_good?"
print("Original string is:" +str(string1))
result = string.capwords(string1.replace("_","").replace(",",""))
print("After conversion:" +str(result))