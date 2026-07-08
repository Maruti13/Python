def Divisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))
    bRet = Divisible(Value)

    if(bRet == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()