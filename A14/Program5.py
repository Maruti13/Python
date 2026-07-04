EvenNumber = lambda No : (No % 2 == 0)

def main():
    Value = int(input("Enter Number : "))

    bRet = EvenNumber(Value)

    if(bRet == True):
        print(f"{Value} is an even number")
    
    else:
        print(f"{Value} is not an even number")

if __name__ == "__main__":
    main()