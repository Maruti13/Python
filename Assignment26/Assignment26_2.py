class Circle:
    # Class Variable
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, Value):
        self.Radius = Value

    def CalculateArea(self, Radius):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self, Radius):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print(f"Radius of circle is : {self.Radius}")
        print(f"Area of circle is : {self.Area}")
        print(f"Circumference of circle is : {self.Circumference}")

def main():
    NoCircles = int((input("Enter number of circles : ")))

    for i in range(NoCircles):
        print("Circle : ",i + 1)
        Value = float(input("Enter radius of circle : "))

        cobj = Circle()
        
        cobj.Accept(Value)
        cobj.CalculateArea(Value)
        cobj.CalculateCircumference(Value)
        cobj.Display()

if __name__ == "__main__":
    main()