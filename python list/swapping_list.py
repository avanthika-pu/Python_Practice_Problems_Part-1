#Swapping two elements in a list
mylist = [1,2,3,4,5]
index_1, index_2 = 1,2
mylist[index_1], mylist[index_2] = mylist[index_2], mylist[index_1]
print(mylist)