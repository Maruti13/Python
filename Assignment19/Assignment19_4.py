from functools import reduce

Size = int(input("Enter number of elements : "))

Data = []

print("Enter elements:")
for i in range(Size):
    No = int(input())
    Data.append(No)

FilterData = list(filter(lambda No: No % 2 == 0, Data))
print("After Filter:",FilterData)

MapData = list(map(lambda No: No * No, FilterData))
print("After Map:",MapData)

Ret = reduce(lambda A, B: A + B, MapData)

print("Addition : ",Ret)