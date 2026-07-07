from functools import reduce

Numbers = list(map(int, input("Enter numbers").split()))

filtered = list(filter(lambda x: 70 <= x <= 90, Numbers))
mapped = list(map(lambda x: x + 10, filtered))
result = reduce(lambda x, y: x * y, mapped)

print("List after filter is : ",filtered)
print("List after map is : ",mapped)
print("Output of reduce is : ",result)