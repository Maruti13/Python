def Prime(No):
    
    if (No <= 1):
        return False
    
    for i in range(2,No):
        if(No % i == 0):
            return False
        
    return True
    
def main():

    Value = int(input("Enter the number : "))
    bRet = False

    bRet = Prime(Value)

    if(bRet == True):
        print(Value,"is a Prime number")

    else:
        print(Value,"is not a Prime number")

if __name__ == "__main__":
    main()