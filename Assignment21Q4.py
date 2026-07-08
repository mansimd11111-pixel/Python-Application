import threading

sum_result = 0
product_result = 1

def Sum(arr):
    global sum_result
    sum_result = sum(arr)

def Product(arr):
    global product_result
    product_result = 1
    for i in arr:
        product_result *= i

arr = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Sum, args=(arr,))
t2 = threading.Thread(target=Product, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum =", sum_result)
print("Product =", product_result)