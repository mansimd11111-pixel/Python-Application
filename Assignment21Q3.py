import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

t1 = threading.Thread(target=Increment)
t2 = threading.Thread(target=Increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter Value:", counter)