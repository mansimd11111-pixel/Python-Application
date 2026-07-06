n = int(input("Enter number: "))

for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()