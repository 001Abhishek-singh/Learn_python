#(18/02/2023) Today we will learn about the os module.

''' The os module in python is a built-in library that provides functions for interacting with the operating system.it allows us to perform a wide variety of tasks,
such as reading and writing files,interacting with the file system,and running system commands.Reading and writing files the os module provides functions for opening,reading and writing files. '''

# so there are various of functions exist in the os modulel so check it from google and try to learn by executing all these function in the program.they have proper os documentation file.

# let's understand it by an example.
import os 
f = os.open("file dictiory",os.O_RDONLY)  # open the file in read-only mode.
user = os.read(f,1024)     # Read the content of the file.
os.close(f)    # close the file
