Even = lambda No: No % 2 == 0

def main():
    Size = int(input("Enter the number of elements :"))

    Numbers = []

    Value = int(input("Enter the numbers :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = list(filter(Even, Numbers))

    print("Even Numbers :",Ret)

if __name__ == "__main__":
    main()