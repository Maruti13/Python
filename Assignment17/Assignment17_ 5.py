def PrimeNumber(No):
    if(No <= 1):
        print("Number cannot be prime")
        return -1
    else:
        for i in range(2, No):
            if(No % i == 0):
                return No

def main():
     Value = int(input("Enter number : "))
     Ret = PrimeNumber(Value)

     print(f"{Value} is a prime number")

if __name__ == "__main__":
    main()