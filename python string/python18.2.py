#finding length of the string 
#3.lambda method
from functools import reduce
str1 = "python"
result = reduce(lambda count, char: count+1, str1, 0)
print(result)