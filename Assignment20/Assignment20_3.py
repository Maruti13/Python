import threading

def EvenList(Data):
    Sum = 0

    for i in Data:
        if(i % 2 == 0):
            print(i)
            Sum = Sum + i

    print("Sum of even elements : ",Sum)
 

def OddList(Data):
    Sum = 0

    for i in Data:
        if(i % 2 != 0):
            print(i)
            Sum = Sum + i

    print("Sum of odd elements : ",Sum)


def main():

    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=EvenList, args=(Data,))
    T2 = threading.Thread(target=OddList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()