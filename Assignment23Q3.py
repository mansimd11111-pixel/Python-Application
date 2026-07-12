from multiprocessing import Pool
import os

def even_count(n):
    return (os.getpid(), n, n // 2)

if __name__ == "_main_":
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(even_count, data)

    for pid, n, count in result:
        print("Process ID :", pid)
        print("Input Number :", n)
        print("Even Number Count :", count)
        print()