import threading

def Maximum(arr):
    print("Maximum element:", max(arr))

def Minimum(arr):
    print("Minimum element:", min(arr))

arr = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Maximum, args=(arr,))
t2 = threading.Thread(target=Minimum, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()