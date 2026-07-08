import Arithmetic

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    print(f"Addition is : {Arithmetic.Add(Value1, Value2)}")
    print(f"Substraction is : {Arithmetic.Sub(Value1, Value2)}")
    print(f"Multiplication is : {Arithmetic.Mult(Value1, Value2)}")
    print(f"Division is : {Arithmetic.Div(Value1, Value2)}")

if __name__ == "__main__":
    main()