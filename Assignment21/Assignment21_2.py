import threading

def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if (i > Max):
            Max = i

    print("Maximum:", Max)


def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if(i < Min):
            Min = i

    print("Minimum:", Min)


def main():

    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=Maximum, args=(Data,))
    T2 = threading.Thread(target=Minimum, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()