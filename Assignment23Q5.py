from multiprocessing import Pool
import math
import os

def factorial_calc(n):
    return (os.getpid(), n, math.factorial(n))

if __name__ == "_main_":
    data = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_calc, data)

    for pid, n, fact in result:
        print("Process ID :", pid)
        print("Input Number :", n)
        print("Factorial :", fact)
        print()