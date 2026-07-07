import threading

def EvenList(arr):
    even = [i for i in arr if i % 2 == 0]
    print("Even Elements:", even)
    print("Sum =", sum(even))

def OddList(arr):
    odd = [i for i in arr if i % 2 != 0]
    print("Odd Elements:", odd)
    print("Sum =", sum(odd))

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=EvenList, args=(lst,), name="EvenList")
t2 = threading.Thread(target=OddList, args=(lst,), name="OddList")

t1.start()
t2.start()

t1.join()
t2.join()