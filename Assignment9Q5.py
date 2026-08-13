def CheckDivisible(No):
    if No % 3 == 0 and No % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")    
        
num = int(input("Enter a number"))
CheckDivisible(num)        