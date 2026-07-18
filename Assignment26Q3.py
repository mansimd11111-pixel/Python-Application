class Arithmetic:
    
    def _init_(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1: "))
        self.Value2 = int(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
         return "Division by zero is not possible"
        return self.Value1 / self.Value2


Obj1 = Arithmetic()
Obj2 = Arithmetic()

print("Enter values for Object 1")
Obj1.Accept()
print("Addition is : ",Obj1.Addition())
print("Subtraction is : ",Obj1.Subtraction())
print("Multiplication is : ",Obj1.Multiplication())
print("Division is : ",Obj1.Division())

print("\nEnter values for Object 2")
Obj2.Accept()
print("Addition is : ",Obj2.Addition())
print("Subtraction is : ",Obj2.Subtraction())
print("Multiplication is : ",Obj2.Multiplication())
print("Division is : ",Obj2.Division())