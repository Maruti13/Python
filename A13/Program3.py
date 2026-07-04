def ChkPerfect(No):

    if No <= 0:
        return False
        
    iSum = 0
    
    for i in range(1, No):
        if No % i == 0:
            iSum = iSum + i 
            
    if iSum == No:
        return True
    else:
        return False

def main():
    
    Value = int(input("Enter the number : "))
    bRet = False

    bRet = ChkPerfect(Value)

    if bRet == True:
        print(Value, "is a Perfect number")
    else:
        print(Value, "is not a Perfect number")

if __name__ == "__main__":
    main()
