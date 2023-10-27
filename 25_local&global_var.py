# today we will learn about the local and global variable.

# variable ---> A variable is a named location in memory that stores a value.in python,we can assign values to variables using the assignment operator.
# local variable ---> it is a variable that is defined within a function and it is only accessible within that function.it is created when the function is called and is destroyed when the function returns.
# global variable ---> it is a variable that is defined outside of a function and it is accesible from within any function in your code.
# The Global keyword ---> The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope(by using this keyword we can convert the local variable into global variable and we can use it from one function to another function without any difficulties).

# let's understand it by an example.
x = 23   # here x act as a global variable.
print(x)

def create():
    y = 'hello this side is abhishek.'
    print(y)     # here y act as local variable.
    print(x)     # as we can see that x is a global variable due to which they run inside and outside the function.

create()

'print(y)' # as we can see this is local variable due to which they run only when function recall itself otherwise they will not run or execute properly.

# let's take an example based on global keyword.
'''user = "This side is abhishek and today i am going to learn about the python."
print(user)
def create2():
    local = "This is totally awesome when anyone going to visit the kedarnath temple." 
    print(local)

create2()'''

'''here we will use the global keyword'''
user = "This side is abhishek and today i am going to learn about the python."
print(user) # here user is a global variable which we will used in our function by using the global keyword for changing the text.

def create2():
    global user
    global local

    local = "This is totally awesome when anyone going to visit the kedarnath temple." 
    print(local)

    user = "NO you should not learning python,i suggest you to learn web deveploment."
    print(user)

create2()
print(local)  # Again we can understand this global keyword concept where we convert the local variable into global variable.
