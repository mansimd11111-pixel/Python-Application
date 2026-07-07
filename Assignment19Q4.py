from functools import reduce

numbers = list(map(int, input("Enter numbers").split()))

filtered = list(filter(lambda x: x % 2 == 0, numbers))
mapped = list(map(lambda x: x * x,filtered))
result = reduce(lambda x, y: x + y,mapped)

print("List after filter is : ",filtered)
print("List after map is : ",mapped)
print("Output of reduce is : ",result)