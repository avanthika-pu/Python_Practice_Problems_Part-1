# smallest number using for loop
a = [10, 20, 30, 40]
smallest = a[0]
for val in a:
    if (val < smallest):
        smallest = val
print(smallest)