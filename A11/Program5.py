def PalindromeNumber(No):
    
    if (No <= 0):
        return 1
    
    iDigit = 0
    iRev = 0
    
    while(No != 0):
        iDigit = No % 10
        iRev = (iRev * 10) + iDigit
        No = No // 10

    return iRev

def main():

    Value = int(input("Enter the number : "))
    iRet = 0

    iRet = PalindromeNumber(Value)

    if(iRet == Value):
        print(Value,"is a Palindrome Number")

    else:
        print(Value,"is not a Palindrome Number")

if __name__ == "__main__":
    main()