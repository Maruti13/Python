def DisplayNumberReverse(No):
    
    for i in range(No,0,-1):
        print(i)

def main():

    Value = int(input("Enter the number : "))

    DisplayNumberReverse(Value)

if __name__ == "__main__":
    main()