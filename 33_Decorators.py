# In this session we will learn about the decorators in oops.

''' Decorator ---> they are powerful and versatile tool that allow us to modify the behavior of functions and methods.they are a way to extend the functionally of a function or method without modifying its source code.
a decorator is a function that takes another function as an argument and return a new function that modifies the behavior of the original function.the new function is often refered to as a"decorator"function.
Syntax of decorator ---> @decorator_function
-- it is often used to add functionally to function and method,such as logging,memorization and access control.'''

# let's take an example on decorators.
def university(fx):
    def mfx():
       print("University provide lessons for better development.")
       fx()
       print("this is a great time for all the students.")
    return mfx

@university     # @ it is a decorator which is used to add or concatenate the value between the functions.
def hello():
    print("hello world")

hello()

# now we will take an example on decorators with arguments.
def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
        return mfx

@greet
def hello():
    print("hello world ")

def add(a,b):
    print(a + b)
hello()
greet(add)(1,2)