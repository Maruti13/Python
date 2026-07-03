def Divisible(No):
    
    if(No % 3 == 0 and No % 5 == 0):
        return True

def main():

    Value = int(input("Enter the number : "))
    bRet = False

    bRet = Divisible(Value)

    if(bRet == True):
        print(Value,"is divisible by 3 and 5")
    
    else:
        print(Value,"is not divisible by 3 and 5")

if __name__ == "__main__":
    main()