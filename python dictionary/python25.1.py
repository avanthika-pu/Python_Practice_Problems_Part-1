#Ways to sort list of dictionaries  – Using lambda function
# reverse method
mydict = [
            {'name':'avanthika', 'score': 45},
            {'name':'manu','score':25},
            {'name':'malu','score':60}
]
sorted_values = sorted(mydict, key=lambda x: x['name'])
print(sorted_values)