#Ways to sort list of dictionaries by values Using lambda function
mydict = [
            {'name':'avanthika','score':45},
            {'name':'manu','score':34},
            {'name':'malu','score':50}
]
sorted_value = sorted(mydict, key = lambda x:x['score'])
print(sorted_value)