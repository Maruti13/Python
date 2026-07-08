def CountDigits(No):
    iSum = 0
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10

    return iSum

def main():
     Value = int(input("Enter number : "))
     Ret = CountDigits(Value)

     print(f"Count of digits is : {Ret}")

if __name__ == "__main__":
    main()