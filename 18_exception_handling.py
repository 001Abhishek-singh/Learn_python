# in this session we will learn about the error handling(try and except method).

'''Exception Handling ---> it is the process of responding to unwanted or unexcepted events when a computer program runs.Exception handling deals with these
events to avoid the program or system crashing and without this process,exceptions would disrupt the normal operation of a program.'''

'''Exception in python ---> python has many built-in-exception that are raised when your program encounters an error.when these exception occur,the python interpreter stops the current process and
passes it to the calling process until it is handled.if not handled the program will crash.'''

'''Python try & except ---> they are used in python to handle errors and exceptions the code in try block runs when there is no error.if the try block catches the error,then the except block is executed.'''
# finally keyword ---> this keyword is use to print the statement in every situation either it is try or except method.
# this will basically use in functions where they use to print the statement effectively in all the condition whether it is try or except.
'''Custom errors ---> here we self generate the error in the programming so that we can handle the error or issue arises in the program which create a good software for the user. for this we use some keylword like:
 "raise" + "type error" by using this keyword we can generate error acc.to need and usage.'''

# we will understand this concept with the help of example.
'''user = input("enter your number: ")
print(f"learning new concept with file handling {user}")
try:
    for i in range(1,11):
        print(f"{int(user)} x {i} = {int(user)*i}")
except Exception as e:
    print("Invalid input")

print("you are good to go......")           # this will also print the statement in both the case(try and in exception)but they do not able to use in functions.

# we will try to understand some more examples.
user = int(input("enter your number: "))
print("we want a even number only.........")
try:
    if user%2 == 0:
        print("Great this is a even number.")
except Exception as e:
    print("the value is not acceptable")

print("only even number is applicable for this program.")'''

# example of finally keyword.
'''def create():
    try:
       user = ["harry","goal","target",34,54,21]
       user_1 = int(input("enter the index no: "))
       print(user[user_1])
    except:
        print("something wrong in the system.....")
    finally:
        print("Good to go....")
create()'''

# example of type error:
'''user = int(input("enter the number between 10 to 20: "))
if user<10 or user>20:
    raise ValueError("You enter a wrong input.")
else:
    print("good to go....")'''

# example of type error:
print("Enter quit.....")
user = input("enter the string: ")
if user == "quit":
    print("well done....")
else:
    raise ValueError("wrong input...")

