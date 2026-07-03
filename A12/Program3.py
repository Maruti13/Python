def Addition(No1, No2):
    
    Sum = 0

    Sum = No1 + No2

    return Sum

def Subtraction(No1, No2):
    
    Sub = 0
    
    Sub = No1 - No2

    return Sub

def Multiplication(No1, No2):
    
    Mult = 1
    
    Mult = No1 * No2

    return Mult

def Division(No1, No2):
    
    Div = 0
    
    Div = No1 // No2

    return Div

def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    iRet = 0

    iRet = Addition(Value1, Value2)
    print("Addition is : ",iRet)

    iRet = Subtraction(Value1, Value2)
    print("Subtraction is : ",iRet)

    iRet = Multiplication(Value1, Value2)
    print("Multiplication is : ",iRet)

    iRet = Division(Value1, Value2)
    print("Division is : ",iRet)

if __name__ == "__main__":
    main()