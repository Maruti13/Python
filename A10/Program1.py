def Table(No):
    
    for i in range(1,11,1):
        mult = No * i
        print(mult)

def main():

    Value = int(input("Enter the number : "))

    Table(Value)

if __name__ == "__main__":
    main()