from functools import reduce

Min = lambda No1, No2: min(No1, No2)

def main():
    Size = int(input("Enter the number of elements :"))

    Numbers = []

    Value = int(input("Enter number :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = reduce(Min, Numbers)

    print(f"Minimum number is :{Ret}")

if __name__ == "__main__":
    main()