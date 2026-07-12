from multiprocessing import Pool
import os

def even_sum(n):
    total = (n // 2) * ((n // 2) + 1)
    return (os.getpid(), n, total)

if __name__ == "_main_":
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(even_sum, data)

    for pid, n, s in result:
        print("Process ID :", pid)
        print("Input Number :", n)
        print("Sum of Even Numbers :", s)
        print()