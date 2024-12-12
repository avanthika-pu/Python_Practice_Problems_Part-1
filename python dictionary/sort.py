#Ways to sort list of dictionaries by values Using itemgetter
from operator import itemgetter
mydict = [
            {'name': 'avanthika', 'score':50},
            {'name': 'maya','score':34},
            {'name':'ammu','score':25}
]
sorted_values = sorted(mydict, key=itemgetter('score'))
print("result is:", sorted_values)