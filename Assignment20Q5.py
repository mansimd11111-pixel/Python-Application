import threading

def Thread1():
    print("Numbers from 1 to 50:")
    for i in range(1, 51):
        print(i, end=" ")

def Thread2():
    print("\nNumbers from 50 to 1:")
    for i in range(50, 0, -1):
        print(i, end=" ")

t1 = threading.Thread(target=Thread1, name="Thread1")
t2 = threading.Thread(target=Thread2, name="Thread2")

t1.start()
t1.join()    

t2.start()
t2.join()