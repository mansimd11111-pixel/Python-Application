from multiprocessing import Pool
import os
import math

def factorial_info(n):
    return (os.getpid(), n, math.factorial(n))

if __name__ == "_main_":
    numbers = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_info, numbers)

    for pid, num, fact in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()