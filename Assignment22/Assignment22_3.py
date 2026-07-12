from multiprocessing import Pool

def Prime(No):
    iCount = 0

    for i in range(2, No + 1):
        if(No % 1 == 0):
            iCount = iCount + 1

    return iCount

def main():
    Size = int(input("Enter number of elements : "))
    Numbers = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Numbers.append(Value)

    pobj = Pool()

    Ret = pobj.map(Prime, Numbers)

    pobj.close()
    pobj.join()

    print(f"Count of prime numbers is : {Ret}")

if __name__ == "__main__":
    main()