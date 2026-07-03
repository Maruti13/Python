def SumDigits(No):
    
    if (No <= 0):
        return 1
    
    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10

    return iSum

def main():

    Value = int(input("Enter the number : "))
    iRet = 0

    iRet = SumDigits(Value)

    print("Sum of Digits is : ",iRet)

if __name__ == "__main__":
    main()