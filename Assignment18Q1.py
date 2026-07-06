def ListSum(Arr):
    return sum(Arr)

n = int(input("Enter number of elements"))
Arr = []

for i in range(n):
    Arr.append(int(input()))
    
print("Sum is : ",ListSum(Arr))    