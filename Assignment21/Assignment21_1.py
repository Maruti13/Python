import threading

def ChkPrime(No):
    if(No <= 1):
        return False

    for i in range(2, No):
        if(No % i == 0):
            return False

    return True

def Prime(Data):
    for i in Data:
        if(ChkPrime(i)):
            print(i)

def NonPrime(Data):
    for i in Data:
        if not ChkPrime(i):
            print(i)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=Prime, args=(Data,))
    T2 = threading.Thread(target=NonPrime, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()