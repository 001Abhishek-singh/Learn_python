# In this session we will learn about the file Input-Output method.

# files are of two types ---> 1) binary files(used for jpeg/png/etc.) (2) text files.
''' Python provides several ways to manipulate files which includes under the file handling.
Opening a file ---> Before we can perform any operation on a file,we must first open it.Python provides the open() function to open a file.
it takes two arguments:the name of the file and the mode in which the file should be opened. the mode can be'r'for read,'w' for write and 'a' for appending. '''
# let's take an example:
user = open('abhishek.txt','r')
''' here the open() function returns a file object that can be used to read from or write to the file,depending on the mode.'''

# Modes in file:
# (1) Read(r) mode ---> This mode opens the file for reading only and gives an error if the file does not exist.this is the default mode if no mode is passed as a parameter.
# (2) Write(w) mode ---> This mode opens the file for writing only and creates a new file if the file does not exist.
# (3) Append(a) mode ---> This mode opens the file for appending only and creates a new file if the file does not exist.
# (4) Create(x) mode ---> This mode creates a file and gives an error if the file already exists.
# (5) Text(t) mode ---> Apart from these modes we also need to specify how the file must be handled.t mode is used to handle text files.t refers to the text mode.there is no difference between r and rt or w and wt since text mode is the default.The defalut mode is 'r'(open for reading text,synonym of 'rt')
# (6) Binary(b) mode ---> used to handle binary files(images,pdf,etc.)

# The 'with' statement ---> we can use the 'with statement' to automatically close the file after we are done with it.

# readlines() method ---> This method reads a single line from the file.if we want to read multiple lines,we can use a loop.it will read all the lines of the file and returns them as a list of strings.
# writelines() method ---> This method used in python to writes a sequence of strings to a file.The sequence can be any iterable object,such as a list or a tuple.This will write the strings in the lines list to the file directiory(xyz.txt).the \n characters are used to add newline characters are used to add newline characters to the end of each string.
# Note: the writelines() method does not add newline characters between the strings in the sequence.if we want to add newlines between the strings,we can use a loop to write each string separately.
# seek() method ---> it allows us to move the current position within a file to a specific point.The position is specified in bytes,and we can move either forward or backward from the current position.
# tell() method ---> it returns the current position within the file,in bytes.This can be useful for keeping track of our location within the file or for seeking to a specific position relative to the current position.
# truncate() method ---> when we open a file in python using the open function we can specify the mode in which we want to open the file.if we specify the mode as 'w' or 'a',the file is opened in write mode and we can write to the file.however,if we want to truncate the file to a specific size,we can use the truncate function.

# let's understand it by an example where we will use 'write mode' from file handling.
a = open("abhishek.txt",'w')
a.write("This side is abhishek and i am writing the text here because i want to learn file handling in python programming language.")
a.close() 

# let's take an example on 'read mode' from file handling.
b = open("abhishek.txt",'r')
read = b.read()
print(read)
b.close()

# let's take an example on 'append mode' from file handling.
c = open("abhishek.txt",'a')
c.write("\n you know coding skills is the most essential for any programmer but they all have different technique to solve the problems related to coding.")
c.close()

# let's take an another example based on 'read mode' from file handling.
d = open('abhishek.txt','r')
take = d.read()
print(take)
d.close()

# let's take an example based on with statement.
with open('abhishek.txt','a') as e:
    e.write("\n This is just a trail.")

# let's take an example based on readlines() method.
f = open("vivek.txt",'w')
f.write("hello world \n how are you \n i am fine \n tell me about your self\n nice and today i am going to italy.")
f.close()

g = open("vivek.txt",'r')
while True:
    line = g.readline()
    if not line:       
        break
    print(line)

# let's take an example based on writeline() method.
h = open('vivek.txt','w')
lines = ['abhishek\n','vivek\n','shivam\n','ashish\n','avinash\n']
h.writelines(lines)  
h.close()

# let's take an another example based on writeline() method.
h = open('vivek.txt','w')
lines = ['football','tennis','cricket','badminton']
for line in lines:
    h.write(line + '\n')
h.close()

# let's take an example based on seek function.
with open('vivek.txt','r') as value:
    value.seek(4)  # it will Move to the 4th byte in the file
    data = value.read(3) # it will Read the next 3 bytes after moving the initial 4 byte from the file.
    print(data)
    print(type(value))

# let's take an example based on tell function.
with open('vivek.txt','r') as value:
    value.seek(4) # it will move to the 4th byte in the file
    position = value.tell() # it will tell the current position from where it will read the file
    data = value.read(3)  # it will read the byte from the file.
    print(position)
    print(data)

# let's take an example based on truncate function.
with open('vivek.txt','w') as value:
    value.write('Hello world ')
    value.truncate(5)