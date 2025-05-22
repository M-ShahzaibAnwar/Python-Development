''' Task 3: Calculator class
Methods: add(x, y), subtract(x, y), multiply(x, y), divide(x, y)

Take input from user and perform selected operation'''

class Calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y==0:
            print("Cannot divide by 0")
        else:
            return x/y
    
#cal object
cal=Calculator()

#take input from user
print("chose the operation : Add,Subtract,multiply,divide")
operation=input("Enter Opertaion: ").strip().lower()#strip remove extra spaces,#lower converts into small case

x=float(input("Enter first number"))
y=float(input("Enter Second Number"))


#peroform operation
if operation == "add":
    print("result:",cal.add(x,y))
elif operation == "subtract":
    print("result :", cal.subtract(x,y))
elif operation=="multiply":
    print("result  :",  cal.multiply(x,y))
elif operation=="divide":
    print("result :", cal.divide(x,y))
else:
    print('error input')