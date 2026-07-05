Largest = lambda x, y, z: x if x >= y and x >= z else (y if y >= z else z)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest =", Largest(a, b, c))