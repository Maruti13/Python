from functools import reduce

def ChkPrime(No):

    if(No <= 1):
        return False

    for i in range(2, No):
        if(No % i == 0):
            return False

    return True


Size = int(input("Enter number of elements : "))

Data = []

print("Enter elements:")
for i in range(Size):
    No = int(input())
    Data.append(No)

FilterData = list(filter(ChkPrime, Data))
print("After Filter:",FilterData)

MapData = list(map(lambda No: No * 2, FilterData))
print("After Map:",MapData)

Ret = reduce(lambda A, B: A if A > B else B, MapData)

print("Maximum is : ",Ret)