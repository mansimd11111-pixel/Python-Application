class Circle:
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter Radius : "))
        
        
    def CalculateCircumference(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        
    def Display(self):
        print("Radius is : ",self.Radius)  
        print("Area is : ",self.Area)
        print("Circumference is : ",self.Circumference)
        
        
Obj1 = Circle()
Obj2 = Circle()

print("Enter details for Circle 1")
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

print("Enter details for Circle 2")
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()   
        
                      
    

