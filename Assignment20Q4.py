import threading

def Small(s):
    c = sum(1 for ch in s if ch.islower())
    print("\nThread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase Letters:",c)

def Capital(s):
    c = sum(1 for ch in s if ch.isupper())
    print("\nThread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase Letters:",c)

def Digits(s):
    c = sum(1 for ch in s if ch.isdigit())
    print("\nThread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits:", c)

text = input("Enter String:")

t1 = threading.Thread(target=Small, args=(text,), name="Small")
t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
t3 = threading.Thread(target=Digits, args=(text,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()