# in this session we will learn about the lambda function.

# Lambda function ---> it is a one liner function which is easy to use by the programmer.sometime it is also known as anonymous function.
# function can be passes as an argument in another function.
''' Lambda function are often used in situations where a small function is required for a short period of time.they are commonly used as an arguments to higher-order function,such as map,filter and reduce.'''

# let's understand it by an example.
'''user = lambda X,y: X+y  # with the help of lambda we can create a function.where we don't use the def keyword instead of def we will make a variable and where we put lambda in that variable.
print(user(23,43)) '''

# let's understand it by another example. 
'''user_2 = lambda x,y,z,p: (x+y)*(y-z)*(z*p)*(p/x)
print(user_2(23,123,54,65))'''   # it will take multiple argument for problem solving.but this cannot be used for bigger function.

# Note: try to understand that how one function passes as an argument in another function.
'''def first(sec,value):
    return 6 + sec(value)
print(first(lambda x: x*x,2))'''

