# (23\02\2023) in this session we will learn about the class and object in Object-oriented programming.

# Class ---> A class is a blueprint or a template for creating objects,providing initial values for state(members variable or attributes) and implementation of behavior(member function or method.) user defined objects are created by using class keyword.
# Object ---> Object is the instance of the class used to access the program of the class.
# Self parameter ---> The self parameter is a reference to the current instance of the class,and it is used to access variables that belong to the class.It must be provided as the extra parameter inside the method defination.

# now let's we create a class for proper understanding.
class first:   # here first reffered as name of the class.
    name = 'ABHISHEK'
    age = 21            # name,age,hobby these things reffered as object or properties in the class.
    hobby = "cycling"
    def info(self):  # in class, info function called as method and in each method 'self keyword' is most essential to perform it. 
        print(f"{self.name} is the very sky person at the age of {self.age}")
    
a = first()    # here we are calling the class.
b = a.name = "shivam"
c = a.age = 23
d = a.hobby = "football"
print(b,c,d)
a.info()

# let's make an another example on class.
class second:
    name = "shalini"
    age = 21
    height = "5'8"
    loc = "hisar"
    edu = "b.tech"
    x = int(input("enter your first number: "))
    y = int(input("enter your second number: "))
    def info_2(self,x,y):
        x
        y
        c = x+y
        print(f"this is my first sum ",c,{self.name},"this is my first number{self.x} and this is my second number{self.y}")  
        
a = second()
b = second()
c = second()
a.name
b.name = "ashish"
c.name = "avinash"
a.age
b.age = 23
c.age = 19

a.height
a.height = "5'6"
b.height = "5'8"
c.height = "6'2"

a.loc
b.loc = "bihar"
c.loc = "delhi"

a.edu
print(f"my name is {a.name},i am {a.age} year old ,my height is {a.height},live in {a.loc},and currently i am pursuing my {a.edu} from GJU.")
print(f"my name is {b.name},i am {b.age} year old ,my height is {b.height},live in {b.loc},and currently i am pursuing my {b.edu} from GJU.")
print(f"my name is {c.name},i am {c.age} year old ,my height is {c.height},live in {c.loc},and currently i am pursuing my {c.edu} from GJU.")
a.info_2()

