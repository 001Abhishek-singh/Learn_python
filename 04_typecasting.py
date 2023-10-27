# in the session we will learn about the typecasting or typeconversion.

# Typecasting ---> it is a method to convert the one datatype into another datatype this is known as typecasting and also known as type conversion.
# Python supports a wide variety of function or method like: int(),float(),str(),ord(),hex(),oct(),tuple(),list(),dic(),set(),etc for typecasting in python.
# typecasting is of two types: 1) Explicit typecasting 2) Implicit typecasting
# 1) Explicit typecasting ---> the conversion of datatype from one form to another by the programmer or developer manually as per the requirements,this is known as explicit typecasting.
# 2) Implicit typecasting ---> the conversion of datatype from one form to another by the python itself that is known as implicit typecasting.
'Python converts a smaller datatype to a higher datatype to prevent data loss.'

a = 34
b = 12.56
c = a+b
print(c)   # here we saw the example of implicit typecasting.

d = "24"
e = 12
f = int(d)+ e
print(f)   # here we saw the example of explicit typecasting.

user = "TONY STARK"
user2 = 1
user3 = user +" "+ str(user2)
print(user3)
