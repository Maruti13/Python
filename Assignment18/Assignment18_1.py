def Addition(Arr):
    Sum = 0

    for i in Arr:
        Sum = Sum + i

    return Sum


def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = Addition(Data)

    print(f"Addition is : {Ret}")


if __name__ == "__main__":
    main()