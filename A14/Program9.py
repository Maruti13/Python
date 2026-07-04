Mult = lambda No1, No2 : (No1 * No2)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    iRet = Mult(Value1, Value2)

    print("Multiplication is :",iRet)

if __name__ == "__main__":
    main()