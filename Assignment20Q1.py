import threading          

def Even():
    print("Even Numbers")
    
    for i in range(2, 21, 2):
        print(i,end=" ")
        
def Odd():
    print("\nOdd Numbers")
    for i in range(1, 20 , 2):
        print(i,end =" ")
        
        
R1 = threading.Thread(target=Even, name = "Even")
R2 = threading.Thread(target=Odd, name = "Odd")

R1.start()
R2.start()

R1.join()
R2.join()             