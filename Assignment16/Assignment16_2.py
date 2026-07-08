def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    bRet = ChkNum(Value)

    if(bRet == True):
        print(f"{Value} is an even number")
    else:
        print(f"{Value} is an odd number")

if __name__ == "__main__":
    main()