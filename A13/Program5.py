def Grade(Marks):
    
    if(Marks >= 75):
        print("Distinction")

    
    elif(Marks >= 60):
        print("First Class")


    if(Marks >= 50):
        print("Second Class")


    if(Marks < 50):
        print("Fail")

def main():

    Value = int(input("Enter the Marks : "))

    Grade(Value)

if __name__ == "__main__":
    main()