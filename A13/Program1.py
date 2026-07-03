def RectArea(Length, Width):
    
    Area = Length * Width

    return Area

def main():

    Value1 = int(input("Enter length of rectangle : "))
    Value2 = int(input("Enter width of rectangle : "))
    Ret = 0

    Ret = RectArea(Value1, Value2)

    print("Area of rectangle is : ",Ret)
    
if __name__ == "__main__":
    main()