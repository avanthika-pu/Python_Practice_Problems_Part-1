#ways to sort the dictionary values by itemgettr, by reverse method
from operator import itemgetter
mydict = [
            {'name':'avanthika','score':35},
            {'name':'manu','score':24},
            {'name':'ammu','score':50}
]
sorted_values = sorted(mydict, key=itemgetter('name','score'),reverse = True)
print("Result:", sorted_values)