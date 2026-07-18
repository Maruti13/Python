class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if(self.Value < 2):
            return False

        for i in range(2, self.Value):
            if(self.Value % i == 0):
                return False

        return True

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i

        if(Sum == self.Value):
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ", end=" ")

        for i in range(1, self.Value + 1):
            if(self.Value % i == 0):
                print(i)

        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if(self.Value % i == 0):
                Sum = Sum + i

        return Sum


def main():
    NoObjects = int(input("Enter number of objects : "))

    for i in range(NoObjects):
        print("Object", i + 1)

        Value = int(input("Enter number : "))

        obj = Numbers(Value)

        print(f"Prime : {obj.ChkPrime()}" )
        print(f"Perfect : {obj.ChkPerfect()}")

        obj.Factors()

        print(f"Sum of Factors : {obj.SumFactors()}")

if __name__ == "__main__":
    main()