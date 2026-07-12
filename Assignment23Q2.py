from multiprocessing import Pool
import os

def odd_sum(n):
    m = (n + 1) // 2
    total = m * m
    return (os.getpid(), n, total)

if __name__ == "_main_":
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(odd_sum, data)

    for pid, n, s in result:
        print("Process ID :", pid)
        print("Input Number :", n)
        print("Sum of Odd Numbers :", s)
        print()