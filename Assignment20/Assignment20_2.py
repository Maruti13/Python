import threading

def EvenFactor(No):
    Sum = 0

    for i in range(1, No + 1):
        if(No % i == 0):
            if(i % 2 == 0):
                print(i)
                Sum = Sum + i

    print("Sum of Even Factors:",Sum)


def OddFactor(No):
    Sum = 0

    for i in range(1, No + 1):
        if(No % i == 0):
            if(i % 2 != 0):
                print(i)
                Sum = Sum + i

    print("Sum of Odd Factors:",Sum)


def main():

    Value = int(input("Enter number : "))

    T1 = threading.Thread(target=EvenFactor, args=(Value,))
    T2 = threading.Thread(target=OddFactor, args=(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()