def CircleArea(Radius):
    
    Area = 3.145 * Radius * Radius

    return Area

def main():

    Value = int(input("Enter radius of circle : "))
    Ret = 0

    Ret = CircleArea(Value)

    print("Area of circle is : ",Ret)
    
if __name__ == "__main__":
    main()