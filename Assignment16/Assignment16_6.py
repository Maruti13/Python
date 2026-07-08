def ChkNum(No):
    if(No >= 1):
        return 1
    
    elif(No < 0):
        return -1
    
    else:
        return 0

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkNum(Value)
    
    if(Ret == 1):
        print(f"{Value} is a positive number")

    elif(Ret == -1):
        print(f"{Value} is a negative number")

    else:
        print(f"{Value} is zero")

if __name__ == "__main__":
    main()