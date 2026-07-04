OddNumber = lambda No : (No % 2 != 0)

def main():
    Value = int(input("Enter the number : "))

    bRet = OddNumber(Value)

    if(bRet == True):
        print(f"{Value} is an odd number")

    else:
        print(f"{Value} is an odd number")

if __name__ == "__main__":
    main()