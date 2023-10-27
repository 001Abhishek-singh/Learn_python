# Today we are going to learn about the doc-string.

# Docstring ---> python docstring are the string literals that appear right after the defination of a function,method,class or module.
# it help to understand a function/object/class in a better way.
# Note: if we change the comment than program does not change but if we change the docstring than program will be change.
''' difference between comments and docstring.
comment ---> comments are description that help programmer better understand the intent and functionality of the program.they are completely ignored by the python interpretor
docstring ---> docstrings are strings used right after the definition of a function,class,module,method.they are used to document our code.we can access the docstring by using the doc attribute.'''


def google(n):
    '''Takes in a number,returns the square of n'''  # here this statement is a docstring.
    print(n**2)                         # it(docstring) will always written either below the function name or above the function body.
google(5)
print(google.__doc__)

def save():
    ''' this function is used to create the GUI page which is design by the dexterous group of industries.'''
a = "let's learn together"
print(a)
print(save.__doc__)

def create(a,b):
    '''we make a function to add two number'''   # here this statement is a docstring.it will always written either below the function name or above the function body
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = a + b
print(c)
print(create.__doc__)    # whenever we want to use docstring than firstly we will write the function name than dot(.) than __doc__.ex: create.__doc__
create(1,1)

