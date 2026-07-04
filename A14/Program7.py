Divisible = lambda No : (No % 5 == 0)

def main():
    Value = int(input("Enter the number : "))

    iRet = Divisible(Value)

    if(iRet):
        print(f"{Value} is Divisible by 5")

    else:
        print(f"{Value} is not Divisible by 5")

if __name__ == "__main__":
    main()