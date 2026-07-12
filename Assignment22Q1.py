from multiprocessing import Pool

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) //6

if __name__ == "_main_":
    numbers = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_of_squares, numbers)

    print(result)