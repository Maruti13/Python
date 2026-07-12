from multiprocessing import Pool
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    print("Process ID : ",os.getpid())
    print("Input number : ",No)
    print("Factorial : ",Fact)
    print()

def main():
    Size = int(input("Enter number of elements : "))
    Numbers = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Numbers.append(Value)

    pobj = Pool()

    pobj.map(Factorial, Numbers)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()