class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self, No1, No2):
        self.Value1 = No1
        self.Value2 = No2
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            Div = self.Value1 / self.Value2
            return Div
        except ZeroDivisionError:
            return "Division by zero is not possible"

def main():
    NoObj = int(input("Enter number of objects : "))

    for i in range(NoObj):
        print("Object : ",i + 1)

        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))

        aobj = Arithmetic()

        aobj.Accept(No1, No2)

        print(f"Addition is : {aobj.Addition()}")
        print(f"Substraction is : {aobj.Substraction()}")
        print(f"Multiplication is : {aobj.Multiplication()}")
        print(f"Division is : {aobj.Division()}")

if __name__ == "__main__":
    main()