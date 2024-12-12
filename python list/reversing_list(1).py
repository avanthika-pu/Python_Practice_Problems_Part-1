# reversing using list comprehension
mylist = [10,20,30,40]
rev = [mylist[i] for i in range (len(mylist) -1, -1, -1)]
print(rev)