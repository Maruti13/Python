Square = lambda No: No * No

def main():
    Size = int(input("Enter number of elements :"))

    Numbers = []

    Value = int(input("Enter the numbers :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = list(map(Square, Numbers))

    print("Square List :",Ret)

if __name__ == "__main__":
    main()