# in this session we will learn about the map,filter and reduce function.

'''In python the map,filter,reduce functions are built-in-functions that allow us to apply a function to a sequence of elements and return a new sequence.
these functions are known as higher-order function,as they take other functions as argument.'''

# Map ---> The map function applies a function to each element in a sequence and returns a new sequence containing the transformed element.the map function has following syntax.
''' syntax of map function ---> map(function,iterable).The function argument is a function that is applied to each element in the iterable argument.
the iterable argument can be a list,tuple or any otheer iterable object.'''

# Filter ---> The filter function filters a sequence of elements based on a given predicate function that returns a boolean value and return a new sequence  containing only the elements that meet the predicate.the filter function has following syntax.
''' syntax of filter function ---> filter(function,iterable).The predicate argument is a function that returns a boolean value and its applied to each element in the iterable argument.it can be list,tuple or any other iterable object.'''

# Reduce ---> The reduce function is a higher order function that applies a function to a sequence and returns a single value.it is a part of the function reduce in python and it has following synatax.
''' synatx of reduce function ---> reduce(function,iterable).The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element,and so on.the reduce function returns the final result.'''

# let's take an example on map function.
def cube(x):
    return x*x
print(cube(3))
mylist = [12,43,53,13,61]
mynewlist = list(map(cube,mylist))  # here map object in output convert into the list by list keyword.
print(mynewlist)

# let's take an example on filter function.
def filter_function(a):
    return a>15

mylist = [12,43,53,13,61]
l = list(filter(filter_function,mylist))
print(l)

# let's take an example on map function by using the lambda function.
mylist = [12,43,53,13,61]
l = list(map(lambda x:x*x*x,mylist))
print(l)

# let's take an example on reduce function.
from functools import reduce
numbers = [12,53,7,6,3]
multi = reduce(lambda x,y:x * y,numbers)
print(multi)