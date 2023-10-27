# In this session we will learn how importing work in python.

'''Import function ---> Importing in python is the process of loading code from a python module into the current script.This allow us to use the function and variables defined
in the module in the current script,as well as any additional modules that the imported module may depend on.To import a module in python we use the import statement followed by the name of the module.'''
# Once a module is imported we can use any of the functions and variables defined in the module by using the 'dot notation'.
# from keyword ---> this method is used to import only one specific function or one specific variable from that module.
# importing everything (*) ---> It's also possible to import all functions and variables from a module using the * symbol.However,this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
# "as" keyword ---> this method is used to give a short name to that specific function,variable and module.so that we can use these stuff for multiple times in our programming section.
# dir function/method ---> Finally,python has a built-in-function called 'dir' that we can use to view the names of all the functions and variables defined in a module.This can be helpful for exploring and understanding the content of new module.

# let's understand it by an example.
'''import math
a = int(input("enter a number: "))
b = math.pi*a
print(b)'''

# example based on from keyword in import module.
'''from math import sqrt      # here we are importing the sqrt function(specifically) from math module.
a = int(input("Enter your first number: "))
b = sqrt(a)
print(b)'''

# example based on importing everything in import module.
'''from tkinter import *
root = Tk()
root.title("Tkinter")
root.mainloop()'''

# example based on "as" method.
'''from math import sqrt as s
a = int(input("Enter your first number: "))
b = s(a)
print(b)'''

# example based on dir function.
'''import tkinter
print(dir(tkinter))'''

# now we will try to learn how to import files from other folders.
'''from trail import show
show()'''    # this is my first program where i created a program and tried to import that 'trail file' to here.
