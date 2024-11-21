# word frequency using shorthand
test_str = "python is simple, its very simple programming language,this is python programming"
print("original string is:" , str(test_str))
result = {key: test_str.count(key) for key in test_str.split()}
print(result)