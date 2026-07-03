def SumNatural(No):
    
    Sum = 0

    for i in range(1,No + 1):
        Sum = Sum + i
        
    print("Sum of N natural numbers is : ",Sum)

def main():

    Value = int(input("Enter the number : "))

    SumNatural(Value)

if __name__ == "__main__":
    main()