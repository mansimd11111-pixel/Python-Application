def Frequency(arr, no):
    return arr.count(no)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

num = int(input("Enter number to search: "))

print("Frequency =", Frequency(arr, num))