from multiprocessing import Pool
import os

def CountOdd(No):
    Count = 0

    for i in range(1, No + 1):
        if(i % 2 != 0):
            Count = Count + 1
    
    print("Process ID : ",os.getpid())
    print("Input number : ",No)
    print("Count of odd numbers : ",Count)
    print()

def main():
    Size = int(input("Enter number of elements : "))
    Numbers = []

    for i in range(Size):
        Value = int(input("Enter number : "))
        Numbers.append(Value)

    pobj = Pool()
    
    pobj.map(CountOdd, Numbers)
    
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()