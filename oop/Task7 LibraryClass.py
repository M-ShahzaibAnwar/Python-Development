''' Task 6: Library class
Maintain list of books

Methods: add_book(book_name), remove_book(book_name), display_books()'''

class Library:
    def __init__(self):
        self.books=[]
        


    def add_book(self,book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' is added successfuly")
        print(f"Present Books after adding :{self.books}!")

    def remove_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' is removed now")
            print(f"Present Books after removing :{self.books}!")
        else:
            print(f"Error : Book {book_name} is not present")
            print(f"Available Books are : {self.books}!!!")
        
        

    def display_books(self):
        print(self.books)
        

l=Library() #making object
while True:
    print("Choose the operation ... 1 for adding books / 2 for removing books / 3 for dislaying books / 4 for exit :")
    operation=input("Enter the operation :")

    if operation=="1":
        book_name=input("Enter the BOOK name to add:")
        l.add_book(book_name)
    elif operation=="2":
        book_name=input("Enter the BOOK to remove :")
        l.remove_book(book_name)
    elif operation=="3":
        l.display_books()
    elif operation == "4":
        break
else:
    print("Invalid operation!!!")