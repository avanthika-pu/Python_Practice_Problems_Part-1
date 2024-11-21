#finding even length words in a string
str1 = "This is python program"
x = str1.split(" ")
for i in x:
    if len(i)%2==0:
        print(i)



