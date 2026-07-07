import threading

def EvenFactor(no):
    s = 0
    print("Even Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            s += i
    print("\nSum of Even Factors =", s)

def OddFactor(no):
    s = 0
    print("Odd Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            s += i
    print("\nSum of Odd Factors =", s)

num = int(input("Enter Number: "))

t1 = threading.Thread(target=EvenFactor, args=(num,), name="EvenFactor")
t2 = threading.Thread(target=OddFactor, args=(num,), name="OddFactor")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")