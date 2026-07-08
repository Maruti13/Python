def Display(No):
    i = 0
    j = 0

    for i in range(No):
        for j in range(No):
            if(j < No - i):
                print("*",end="  ")
            else:
                print(end=" ")

        print()

def main():
    Value = int(input("Enter value : "))
    Display(Value)

if __name__ == "__main__":
    main()