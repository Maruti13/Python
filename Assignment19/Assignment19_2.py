Multiply = lambda A, B : (A * B)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Multiply(Value1, Value2)

    print(f"Multiplication is : {Ret}")

if __name__ == "__main__":
    main()