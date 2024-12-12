#finding largest element by for loop
a = [10, 20, 30, 40]
largest = a[0]
for val in a:
    if val > largest:
        largest = val
print(largest)