def Frequency(Arr, Value):
    Count = 0

    for i in Arr:
        if (i == Value):
            Count = Count + 1

    return Count


def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    Search = int(input("Enter element to search : "))

    Ret = Frequency(Data, Search)

    print("Frequency is:",Ret)


if __name__ == "__main__":
    main()