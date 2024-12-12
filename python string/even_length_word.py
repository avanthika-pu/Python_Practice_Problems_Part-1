#finding even length words in string suing lambda
str1 = "This is a python program"
words = str1.split(" ")
result = list(filter(lambda x: len(x)%2 == 0, words))
print(result)