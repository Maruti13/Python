from multiprocessing import Pool
import time

def Calculate(No):
    Cal = 0

    for i in range(1, No + 1):
        Cal = i ** 5

    return Cal

def main():
    Size = int(input("Enter number of elements : "))
    Numbers = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Numbers.append(Value)

    pobj = Pool()

    start_time = time.perf_counter()

    Ret = pobj.map(Calculate, Numbers)

    end_time = time.perf_counter()

    pobj.close()
    pobj.join()

    print(f"Sum of squares is : {Ret}")
    print(f"Time Required is : {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()