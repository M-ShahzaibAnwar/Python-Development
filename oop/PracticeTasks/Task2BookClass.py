'''Task 1: Create a Book class
Attributes: title, author, price

Method: display()  show all book details'''
class Book:
    title="DataScience"
    authur="Shahzaib"
    price="Rs500"

    def display(self):
        print(f" Book is :{self.title}\n Authur Name is :{self.authur}\n Price is:{self.price}\n")

my_book=Book()
my_book.display()



#now using Constructor
class Books:
    def __init__(self,title,authur,price):
        self.title=title
        self.authur=authur
        self.price=price
    
    def displays(self):
        print(f"Book Name is :{self.title}")
        print(f"Book Authur Name is :{self.authur}")
        print(f"Book Price is :{self.price}")

my_books=Books("CS","Dogar",850)
my_books.displays()



