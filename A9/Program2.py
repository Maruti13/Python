def ChkGreater(No1, No2):
    
    if(No1 > No2):
        return True

def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    bRet = False

    bRet = ChkGreater(Value1, Value2)

    if(bRet == True):
        print(Value1," is greater than ",Value2)
    
    else:
        print(Value2," is greater than ",Value1)

if __name__ == "__main__":
    main()