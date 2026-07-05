Length = lambda Str: len(Str) > 5

def main():
    Size = int(input("Enter the number of strings :"))

    Words = []

    sValue = int(input("Enter number :"))

    for i in range(Size):
        Words.append(sValue)

    Result = list(filter(Length, Words))

    print(f"Strings having length greater than 5 are : {Result}")

if __name__ == "__main__":
    main()