num = int(input("Enter a number"))

Sum = 0 

while num > 0:
    digit = num % 10
    Sum = Sum + digit
    num = num // 10
    
print("Sum is : ",Sum)    
