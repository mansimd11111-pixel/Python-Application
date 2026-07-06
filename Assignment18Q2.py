def Maximum(Arr):
    return max(Arr)

n = int(input("Enter number of elements"))
Arr = []

for i in range(n):
    Arr.append(int(input()))
    
print("Maximum is : ",Maximum(Arr))    