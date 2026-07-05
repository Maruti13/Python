CountEven = lambda No: No % 2 == 0

def main():
    Size = int(input("Enter the number of elements :"))

    Numbers = []

    Value = int(input("Enter number :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = filter(CountEven, Numbers)

    Count = 0

    for i in Ret:
        Count = Count + 1

    print(f"Count of Even Numbers :{Count}")

if __name__ == "__main__":
    main()