#(19/02/2023) In this session we will learn about the 'is\double equal' keyword in python.

'''In python,is and == both are comparison operators that can be used to check if two values are equal.
IS operator compares the identity of two objects.it will only return True if the objects being compared are the exact same object in memory.
== operator compares the values of the objects.it will return True if the objects have the same value.'''

'''Note: we should remember that in python,strings and integers are immutable,which means that once they are created,their value cannot be changed.
this means that,for strings and integers,is and == will always return the same result.'''

# let's take an example on is and == keyword.
a = 3
b = 3
print(a is b)  # it will check (identity)exact location of the object in memory
print(a == b)  # it will check value in memory
