def Minimum(Arr):
    return min(Arr)

n = int(input("Enter the number of element"))
Arr = []

for i in range(n):
    Arr.append(int(input()))
    
print("Minimum is : ",Minimum(Arr))    