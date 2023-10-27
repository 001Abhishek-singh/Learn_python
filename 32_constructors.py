# In this session we will learn about the constructors in oops.

'''Constructor ---> it is a special method in a class used to create and initialize an object of a class.there are different types of constructor.constructor is invoked automatically when an object of a class is created.
a constructor is a unique function that gets called automatically when an object is created of a class.the main purpose of a constructor is to initialize or assign values to the data members of the class.
it cannot return any value other than none.
    Syntax of constructor ---> def __init__(self):
-- init is one of the reserved function in a python.in oops,it is known as a constructor.we can also create constructor by defining the function name with same class name.'''

# There are two types of constructors.
#(1) Parameterized constructor
#(2) Default constructor

# parameterized constructor ---> when the constructor accepts arguments alongwith self,it is known as parameterized constructor.these arguments can be used inside the class to assign the values to the data members.
# default constructor ---> when the constructor doesn't accepts any arguments from the object and has only one argument,self,in the constructor,it is known as default constructor.

# let's take an example on it.
class pro:      # here we created a class
    def __init__(self,a,b,c):    # here we created a constructor with four arguments self,a,b and c.
        self.a = a                # here we set an specific argument for there usage
        self.b = b                
        self.c = c
    
    def info_3(self):
        print(f"{self.a},{self.b},{self.c}")

anf = pro("harry","23","coder")   # we assigned the value to each argument.
bnf = pro("avinash","23","hello")
acn = pro("google","23","software")

anf.info_3()
bnf.info_3()
acn.info_3()

# let's take a second example on it.
class hero():
    def __init__(self,a):
        self.a = a
    def info_4(self):
        print(f"{self.a} is a trending software company in the world")

b = hero("google")
b.info_4()       

