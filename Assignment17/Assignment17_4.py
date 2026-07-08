def SumFactors(No):
    Sum = 0
    Fact = 1

    for i in range(1,No + 1):
        Fact = Fact * i
        Sum = Sum + Fact

    return Sum

def main():
     Value = int(input("Enter number : "))
     Ret = SumFactors(Value)

     print(f"Sum of factors is : {Ret}")

if __name__ == "__main__":
    main()