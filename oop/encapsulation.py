class Person:
    def __init__(self,name):
        self.__name=name #private variable

    def get_name(self):  #getter methid to access prvate variable
        return self.__name
    
    def set_name(self,new_name):  #setter methud used to update the private variable name 
        self.__name=new_name

#making object
p1=Person("Ali") 

print(p1.get_name())
p1.set_name("Dogar")
print(p1.get_name())