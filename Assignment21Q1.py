import threading

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Prime(arr):
    print("Prime Numbers:")
    for i in arr:
        if isPrime(i):
            print(i, end=" ")
    print()

def NonPrime(arr):
    print("Non-Prime Numbers:")
    for i in arr:
        if not isPrime(i):
            print(i, end=" ")
    print()

arr = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Prime, args=(arr,))
t2 = threading.Thread(target=NonPrime, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()