from functools import reduce 

numbers = [10,45,23,89,12]
result = reduce(lambda x, y: x if x < y else y, numbers)
print(result)