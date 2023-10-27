# today we will learn about the list in python.(25/01/23)

# LIST : 
''' a) List are ordered collection of data items.
    b) they store multiple items in a single variable.
    c) list items are separated by commas and enclosed within square brackets.
    d) list are changeable(mutable),we can change it '''

# Note: Each item/element in a list has its own unique index.this index can be used to access any particular item from the list.
# In a single list each datatype can be inserted without any restriction. 
# we can access list item by using its index with the square bracket syntax[].
# Index is of two types: 1) positive index 2) negative index
# list comprehension ---> list comprehension are used for creating new list from other iterables like list,tuple,dictionaries,
# Syntax of list comprehension: variable name = [expression(item) for item in iterable if condition] 
# List Method: 
# 1) list.sort() ---> this method sorts the list in ascending order.the original list is updated.
# 2) list.reverse() ---> this method sorts the list in reverse order in decending order.the original list is updated.
# 3) list.append() ---> this method add the item at the last position in the list.
# 4) list.index() ---> this method returns the index of the first occurance of the list item.
# 5) list.count() ---> this method return the count of the number of items with the given value.
# 6) list.copy() ---> this method return the copy of the list.this can be done to perform operation on the list without modifying the original list.
# 7) list.insert() ---> this method inserts an item at the given index.user has to specify index and the item to be inserted within the insert() method. 
# 8) list.extend() ---> this method add an entire list or any other collection of data types(list,tuple,set,dic.)to the existing list.
# 9) concatenating the list ---> this method simply add two list.
# 10) NOTE: there are various method present in the list which we have to cover from the official website of python.

user1 = [23,34.54,"nora",True,[23,45,'janvi',False]]
user = [34,56,75,12,32]
print(user)      # -5,-4,-3,-2,-1
print(user[3])
print(user1)
print(user1[2],"my favourite actress.")    # it indicate the positive index.
print(user[-3])
print(user1[-2],"you are a tony stark.")   # it indicate the nagative index.

user2 = [54,7,"bool","toy"]
if "good" in user2:          # To check the string or integer is present or not in the list.by using the "in" variable
    print("yes")
else:
    print("no")

user = [34,56,75,12,32]      # these all method use to print the item of the list by using the index number.
print(user[:])
print(user[1:])
print(user[:-1])
print(user)
print(user[0:5:2])       # this indicate the jump index in the list,here 2 shows that print the next second item from the list

lst = [i*i for i in range(12) if i%2==0]
print(lst)     # this is the example of list comprehension.

a = [32,45,12,87,94,46,56]     # this is the example of list method.
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(a.index(94))

m = a   # here m and a both are a reference of each other.so if we perform changes in m then the change will also shown in a.
m[0] = 4
print(m)
print(a)
m = a.copy()   # here m is copied list of a so if we perform changes in m then the a remains same(it will not change.)
m[0] = 6
print(m)
print(a)

a.insert(1,345)  # here it will insert the 345 at the first(1) index.
print(a)

n = [421,630,389,42]  # here two list n & a will extend(add) with each other.
a.extend(n)
print(a)

n = [421,960,689,785,201]   # here two list simply concatenate(add) with each other.
k = n + a
print(k) 
