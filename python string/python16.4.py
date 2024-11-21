# finding frequency using set() and list() comprehentions
string1 = "python is simple, this is python programming, python programming is simple"
print("original strings is:" +str(string1))
string2 = string1.split()
frequency = {word : string2.count(word)for word in set(string2)}
print("Word frequency is:" +str(frequency))