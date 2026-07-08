def Length(Value):
    return len(Value)

def main():
    Name = input("Enter name : ")

    Ret = Length(Name)

    print(f"Length of {Name} is {Ret}")

if __name__ == "__main__":
    main()