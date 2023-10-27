# today we are going to learn about the f-strings.

''' f-string  ---> it is a new thing formatting mechanism introduced by PEP 498.it is also known as Literal String interpolation or more commonly as f-strings.
the primary focus of this mechanism is to make the interpolation easier. when we prefix the string with the letter"f".the string becomes the f-string itself.
The f-string can be formatted in much same as the str.format() method.'''
# f"this is {put variable name} here f indicate f-string

# this is the example of f-string.
name = input("enter your name: ")
age = int(input("enter your age: "))
letter = "hello world, my name is {} and i am {} year old."
print(f"hello world, my name is {name} and i am {age} year old.")

# now we are going to make a new example of f-string.
google = input("enter your android name: ")
creator = input("created bt whom: ")
age = int(input("enter the age when he created the android name. "))
year = int(input("in which year they had created: "))
print(f"Hey everyone this side is {creator},i am the creator of {google}.i have developed this {google} at the age of {age} in the year of {year}.")

name = "abhishek"
age = "23"
letter2 = "hello world, my name is {} and i am {} year old."
print(f"hello world, my name is {{name}} and i am {{age}} year old.")