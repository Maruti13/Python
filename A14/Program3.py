Max = lambda No1, No2 : (No1 > No2)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Max(Value1, Value2)  

    if(Ret):
        print(f"{Value1} is the maximum number")

    else:
        print(f"{Value2} is the maximum number")

if __name__ == "__main__":
    main()