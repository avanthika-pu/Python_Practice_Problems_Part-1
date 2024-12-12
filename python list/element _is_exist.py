#checking element is existed using a loop
a = [10,20,34,90]
key = 20
flag = False
for val in a:
    if val == key:
        flag = True
        break
if flag:
     print("Element exist")
else:
    print("element not exist")