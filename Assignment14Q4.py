from functools import reduce

Numbers = [1,2,3,4,5]

result = reduce(lambda x, y: x + y,Numbers)
print(reduce)