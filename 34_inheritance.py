# in this session we will learn about the inheritance in oops.

'''Inheritance ---> when a class drives from another class.the child class will inherit all the public and protected properties and methods from the parent class.
in addition,it can have its own properties and methods this is called an inheritance.
Syntax of the inheritance ---> class Baseclass
                              body of Baseclass
                              class derived class(Baseclass)
                              body of derived class'''

# Types of inheritance:
#(1) Single inheritance
#(2) Multiple inheritance 
#(3) Multilevel inheritance
#(4) Herarical inheritance
#(5) Hybrid inheritance

# let's take an example based on inheritance in oops.
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f"this is my room {self.name} and my id is {self.id}")
    
class programmer(Employee):
    def shwo_language(self):
        print("this is default text")

e = Employee("haary","210")
e.showdetails()
f = programmer("coder","234")
f.showdetails()
f.shwo_language()