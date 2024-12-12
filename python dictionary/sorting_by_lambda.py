#Ways to sort list of dictionaries  Using lambda function
#multiple variables
mydict = [
            {'name':'avanthika','score':45},
            {'name':'manu','score':34},
            {'name':'malu','score':50}
]
sorted_values = sorted(mydict, key=lambda x:(x['score'], x['name']))
print(sorted_values)