# finding substringfrom a string using lambda function
string1 = "This is python"
string2 = "python"
x = list(filter(lambda x: (string2 in string1), string1.split()))
print(["YES" if x else "NO"])