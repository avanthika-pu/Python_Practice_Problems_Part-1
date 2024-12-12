# using any() method
a = [1,2,3,4,5]
exist = any(x == 10 for x in a)
if exist:
    print("Element exist in the list")
else:
    print("Element not exist in the list")