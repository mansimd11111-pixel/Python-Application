from functools import MarvellousNum

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False

    return True

def ListPrime(arr):
    total = 0

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            total += i

    return total

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

print("Sum of prime numbers =", ListPrime(arr))