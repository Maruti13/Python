class BookStore:
    # Class Variables
    NoOfBooks = 0

    def __init__(self, Book_Name, Book_Auth):
        self.Name = Book_Name
        self.Author = Book_Auth
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No. of Books : {BookStore.NoOfBooks}")

def main():
    NoObj = int(input("Enter number of objects : "))

    for i in range(NoObj):
        print("Object : ",i + 1)

        Value1 = input(("Enter name of book : "))
        Value2 = input(("Enter name of author : "))

        bobj = BookStore(Value1, Value2)
        
        bobj.Display()

if __name__ == "__main__":
    main()
