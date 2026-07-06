from functools import Arithmetic

def Add(a,b):
    return a + b

def Sub(a,b):
    return a -b

def Muilt(a,b):
    return a * b

def Div(a,b):
    return a / b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", Arithmetic.Add(a, b))
print("Subtraction =", Arithmetic.Sub(a, b))
print("Multiplication =", Arithmetic.Mult(a, b))
print("Division =", Arithmetic.Div(a, b))