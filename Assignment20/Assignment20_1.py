import threading

def Even(No):
    print("Even Numbers:")
    for i in range(1, No + 1):
        print(2 * i)

def Odd(No):
    print("Odd Numbers:")
    for i in range(1, No + 1):
        print((2 * i) - 1)

def main():

    Value = int(input("Enter Number : "))

    T1 = threading.Thread(target=Even, args=(Value,))
    T2 = threading.Thread(target=Odd, args=(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()