def CheckNum(no):
    if no > 0:
        print("Poitive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")    
        
num = int(input("Enter number"))   
CheckNum(num) 