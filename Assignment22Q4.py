from multiprocessing import Pool
import time

def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5
    return total

if __name__ == "_main_":
    numbers = [1000000, 2000000, 3000000, 4000000]

    start = time.time()

    with Pool() as p:
        result = p.map(sum_of_powers,numbers)

    end = time.time()

    print("Results:")
    for n, ans in zip(numbers,result):
        print(f"N = {n} -> {ans}")

    print("Execution Time:", end - start,"seconds")