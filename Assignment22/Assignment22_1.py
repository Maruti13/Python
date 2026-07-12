from multiprocessing import Pool

def SumSquare(No):
    Square = 1
    Sum = 0

    for i in range(1, No + 1):
        Square = i * i
        Sum = Sum + Square

    return Sum

def main():
    Size = int(input("Enter number of elements : "))
    Numbers = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Numbers.append(Value)

    pobj = Pool()

    Ret = pobj.map(SumSquare, Numbers)

    pobj.close()
    pobj.join()

    print(f"Sum of squares is : {Ret}")

if __name__ == "__main__":
    main()