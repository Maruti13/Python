from multiprocessing import Pool
import os

def SumEven(No):
    Sum = 0

    for i in range(1, No + 1):
        if(i % 2 == 0):
            Sum = Sum + i
    
    print("Process ID : ",os.getpid())
    print("Input number : ",No)
    print("Sum of even numbers : ",Sum)
    print()

def main():
    Size = int(input("Enter number of elements : "))
    Numbers = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Numbers.append(Value)

    pobj = Pool()
    
    pobj.map(SumEven, Numbers)
    
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()