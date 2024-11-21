#sorting dictionary by itemgetter by sorting multiple keys
from operator import itemgetter
mydict = [
            {'name':'avanthika','score': 35},
            {'name':'ammu','score': 55},
            {'name':'maya','score':90}
]
sorted_values = sorted(mydict, key=itemgetter('score','name'))
print("Result is:",sorted_values)