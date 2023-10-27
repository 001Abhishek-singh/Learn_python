# Today we will learn about the Enumerate function in python.

# Enumerate function ---> The enumerate function is a built-in-function in python that allows you to loop over a sequence(such as a list,tuple,or string)and get the index and value of each element in the sequence at the same time.

# firstly, we understand what happen if we do not use the enumerate function in python.
'''marks = [12,54,65,23,47]
index = 0
for mark in marks:
    print(mark)                   # this syntax is quit confusing and tricky so that why we are using the enumerate function.
    if (index == 2):
        print("keep learning always....")
    index += 1'''

# let's understand it by an example.
marks = [12,53,54,23,64]
for index,mark in enumerate(marks):
    print(mark)
    if (index == 2):
        print("Keep going ahead.....")

# let's understand it by an another example.
'''fruit = ["apple","banana","papaya","grapes","rasberry","orange","strawberry"]
for index,value in enumerate(fruit):
    print(index,value)'''

'''As we can see the enumerate function returns a tuple containing the index and value of each element in the sequence.we can use the for loop
to unpack these tuples and assign them to variables,as shown in the example.'''

# Note: we can change the 'starting index number' by using the enumerate function.
fruit = ["apple","banana","papaya","grapes","rasberry","orange","strawberry"]
for index,value in enumerate(fruit,start=2):   # here we can set the index number from any value according to our convinency.
    print(index,value)   
