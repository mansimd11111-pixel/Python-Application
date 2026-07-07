from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers: ").split()))

filtered = list(filter(is_prime, numbers))
mapped = list(map(lambda x: x * 2, filtered))
result = reduce(lambda x, y: x if x > y else y, mapped)

print("List after filter =", filtered)
print("List after map =", mapped)
print("Output of reduce =", result)