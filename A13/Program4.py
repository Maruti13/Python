def DisplayBinary(No):

    binary = bin(No)
    print("Binary of",No,"is",binary)

def main():

    Value = int(input("Enter the number : "))
    DisplayBinary(Value)

if __name__ == "__main__":
    main()
