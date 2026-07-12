from multiprocessing import Pool

def prime_count(n):
    count = 0

    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1

    return (n, count)

if __name__ == "_main_":
    numbers = [10000, 20000, 30000, 40000]

    with Pool() as p:
        result = p.map(prime_count, numbers)

    for n, count in result:
        print(f"Prime numbers between 1 and {n}: {count}")