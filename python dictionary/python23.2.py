#remove key item from dictionary
#3.popitem()method
mydict = {'a':10, 'b':20,'c':30}
key, value = mydict.popitem()
print(f"Removed key:{key}, removed value:{value}")