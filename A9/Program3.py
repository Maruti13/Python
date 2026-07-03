def Square(No):
    
    Ans = No * No

    return Ans

def main():

    Value = int(input("Enter the number : "))
    iRet = 0

    iRet = Square(Value)

    print("Square of the number is : ",iRet)

if __name__ == "__main__":
    main()