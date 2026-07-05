Divisible = lambda No: No % 3 == 0 and No % 5 == 0

def main():
    Size = int(input("Enter the number of elements :"))

    Numbers = []

    Value = int(input("Enter number :"))

    for i in range(Size):
        Numbers.append(Value)

    Ret = list(filter(Divisible, Numbers))

    print(f"Numbers divisible by 3 and 5 are :{Ret}")

if __name__ == "__main__":
    main()