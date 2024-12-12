#finding substring in a string using count() method
def check(s2, s1):
    if(s2.count(s1) > 0):
        print("Yes")
    else:
        print("No")
s2 = "This ia s python program"
s1 = "pythons"
check(s2, s1)