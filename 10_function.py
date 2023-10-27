# today we will learn about the function concept.

'''Function ---> a function is a block of code that perform a specific task whenever it is called.in bigger program,where we 
have large amount of code.it is advisible to create or use existing function that make th eprogarm organized and neat or clean'''
# function is of two types:
# 1) Built-in-function ---> these functions are defined and pre-coded in python.for ex: are -- min(),max(),sum(),range(),tuple(),set(),etc.
# 2) User-defined function ---> it is created by the programmer to perform various tasks acc.to need of the code. 
'''syntax: def function_name(parameter/argumnt):  for user-defined function.'''
# Function arguments and return statement ---> there are of four type of arguments that is given as: 
# a) Default arguments
# b) Keyword arguments
# c) Variable arguments
# d) Required arguments
# scope of the variable ---> part of the program in which a variable is accessible is called its scope.
# lifetime of the variable ---> duration for which the variable exists is called its lifetime.
'''In case of nested functions(function inside another function),the inner function can access variables defined in both outer as well as inner function,but the outer function can
access variables defined only in the outer function'''

'''If a variable in the inner function is defined with the same name as that of a variable defined in the outer function,then a new variable is created in the inner function.'''

'''Resolutin of names ---> scope defines the visibility of a name within a block.if a local variable is defined in a block,its scope is that particular block.if it is defined in a functin
,then its scope is all blocks within that function.when a variable name is used in a code block ,it is resolved using the nearest enclosing scope.if no variable of that names is found ,then NameError is raised.'''

'''The return statement must appear within the function.once we return a value from a function,it immediately exits that function.therefore,any code written after the return statement is 
never executed.'''

# Note: Every function encapsulates a set of operations and when called it returns the information to the calling program.
# Note: Functions provide better modularity for our application and a high degree of code reuse.
# Note: Function naming follows the same rules of writing identifiers in python.
# Note: the words before parentheses specifies the function name,and the comma - separated values inside the parentheses are function arguments.
# Note: the indented statements from body of the function.
# Note: the parameter list in the function definition as well as function declaration must match with each other.
# Note: it is a logic error if the arguments in the function call are placed in a wrong order.
# Note: List of variables used in function call is known as the actual parameter list.the actual parameter list may be variable names,expressions,or constants.
# Note: we can call a function from another function or directly from the python prompt.
# Note: the function parameter list must be separated with commas.(a,b,c) 
# Note: trying to access local variable outside the function produces an error.
# Note: we cannot assign value to a variable defined outside a function without using the global statement.
# Note: arguments are specified within parentheses.if there is more than one argument,then they are separated by using the comma.
# Note: try to avoid the use of global variables and global statement.
# Note: a return statement with no arguments is the same as return None.expression for return statement is return[expression],here expression is optional
# Note: a function may or may not return a value.the return statement is used for two things.(1) return a value to the caller (2) to end and exit a function and go back to its caller. 
# Note: the return statement cannot be used outside of a function definition.

'''Local variable ---> they are defined within a function and it is local to that function.they can be accessed from the point of its definition until the end of the block in which it is defined.
they are not related in any way to other variables with the same names used outside the function.'''

'''Global variable ---> they are defined in the main body of the program file.they can be accessed throughout the program file.global variables are accessible to all functions in the program.'''


def average(a,b):     # in this function a & b is required arguments.
    c = int(input("enter the first number: "))
    d = int(input("enter the second number: "))
    e = c+d
    print("this is the final",e,"answer")
average(1,1)

def cool(c,d):
    c = int(input("enter the first number: "))
    d = int(input("enter the second number: "))
    f = c*d
    e = c+d
    g = c-d
    h = c/d 
    print("the answer is given as",f,"as multiplication",e,"as addition",g,"as subtraction",h,"as divide")
cool(1,1) 
                                                                                  
def save(a=4,b=2): # here default arguments are used.(b=2 used as default argument)
    add = a+b
    print(add)
save(34)

def good(b=34,a=21): # here keyword argument are used where order of the variable does not matter.
    add = a+b
    print(add)
good() 

def create():
    pass            # here pass indicate that we will store it for futher usage or need.

def make(a=4,b=8):
    a = int(input("enter the number: "))
    b = int(input("enter the second number: "))
    c = a+b
    return c
