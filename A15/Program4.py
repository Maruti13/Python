from functools import reduce

Add = lambda No1, No2: No1 + No2

def main():
    Size = int(input("Enter the number of elements :"))

    Numbers = []

    Value = int(input("Enter number :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = reduce(Add, Numbers)

    print(f"Addition of all numbers is :{Ret}")

if __name__ == "__main__":
    main()