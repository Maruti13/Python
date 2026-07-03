def CountDigits(No):
    
    if (No <= 0):
        return 1
    
    iDigit = 0
    iCount = 0

    while(No != 0):
        iDigit = No % 10
        iCount = iCount + 1
        No = No // 10

    return iCount

def main():

    Value = int(input("Enter the number : "))
    iRet = 0

    iRet = CountDigits(Value)

    print("Count of Digits is : ",iRet)

if __name__ == "__main__":
    main()