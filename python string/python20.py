#program to accept the string which contain all vowels..
def check_all_vowels(input_str):
    input_str = input_str.lower()
    vowels = {'a','e','i','o','u'}
    if vowels.issubset(set(input_str)):
        return True
    else:
        return False
    
input_str = input("Enter a string:")
if check_all_vowels(input_str):
    print("String contain all vowels")
else:
    print("String doesnt contain all vowels")

