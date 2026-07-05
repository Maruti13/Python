from functools import reduce

Max = lambda No1, No2: max(No1, No2)

def main():
    Size = int(input("Enter the number of elements :"))

    Numbers = []

    Value = int(input("Enter number :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = reduce(Max, Numbers)

    print(f"Maximum number is :{Ret}")

if __name__ == "__main__":
    main()