def Display(No):
    i = 0
    j = 0

    for i in range(1,No + 1):
        for j in range(1,No + 1):
            print(j,end=" ")
            j = j + 1

        print()

def main():
    Value = int(input("Enter value : "))
    Display(Value)

if __name__ == "__main__":
    main()