def Cube(No):
    
    Ans = No * No * No

    return Ans

def main():

    Value = int(input("Enter the number : "))
    iRet = 0

    iRet = Cube(Value)

    print("Cube of the number is : ",iRet)

if __name__ == "__main__":
    main()