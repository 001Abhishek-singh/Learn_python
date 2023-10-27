# Today we will learn about the set object in python.

''' Sets ---> sets are unordered collection of data items.they store multiple items in a single variable.set items are separated by commas and enclosed by commas and 
enclosed within curly brackets{}.sets are unchangeable,meaning you cannot cahnge items of the set once created.sets do not contain duplicate items.'''

# Set Method:
# 1) union() method ---> this method prints all items that are present in the two sets.union method returns a new set after accomplishing the task.
# 2) update() method ---> this method print all items that are present in the two sets.it adds items into the existing set from another set.
# 3) intersection() method ---> this method prints only items that are similar to both the sets.it returns a new set.
# 4) intersection_update() method ---> this method prints only items that are similar to both the sets.it updates into the existing set from another set.
# 5) symmetric_difference() method ---> this method prints only items that are not similar to both the sets.it return the new set.it is basically the difference of union and intersection.
# 6) symmetric_difference_update() method ---> this method prints only items that are not similar to both the sets.it updates into the existing set from another set.it is basically the difference of union and intersection.
# 7) difference() method ---> this method prints only items that are only present in the original set and not in both the sets.it return the new sets.
# 8) difference_update() method ---> this method prints only items that are only present in the original set and not in both the sets.it updates into the existing set from another set.
# 9) isdisjoint() method ---> this method checks if items of given set are present in another set.this method return false if items are present else it return true.
# 10) issuperset() method ---> this method checks if all the items of a particular set are present in the original set.it return true if all the items are present otherwise it will return false when items are not present in it.
# 11) issubset() method ---> this method checks if all the items of the original set are present in the particular set().it return True if all the items are present else it return false.
# 12) add() method ---> this method simply add a single item to the set use the add() method.
# 13) remove()/discard() ---> this method simply remove or discard the single item from the set.
# 14) pop() ---> this method remove the last item of the set but the catch is that we don't know which item gives popped as sets are unordered.we can access the popped item if you assign the pop() method to a variable.
# 15) DEL ---> Note: this is a keyword not a method which is use to delete the set entirely.
# 16) clear() method ---> this method clears all items in the set and prints an empty set.

user = {34,54,34,54,23,64,23,34,34,'nora',"hritik roshan"}
print(user)

# actually this is an example of empty set but as we check the type order then it display that it 'not a set',it is "dictionary datatype".
# Note: the syntax of both set and dictionary start with curly bracket as well as end with same curly bracket.
user1 = {}
print(type(user1))

# this method gives the empty set datatype.
user2 = set()
print(type(user2))

# accessing set items:
user = {34,54,34,54,23,64,23,34,34,'nora',"hritik roshan"}
for items in user:                # here i is just a variable
    print(items)

# this is example of union of set.
a = {122,23,65,34}
b = {34,64,98,36}
print(a.union(b))

# this is example of update of set.
a = {12,43,65,98}
b = {56,74,89,32}
a.update(b) # here value of set a updated by value of set b.
print(a,b)

# this is example of intersection of set.
a = {45,23,87,98}
b = {45,87,21,78}
print(a.intersection(b))

# this is the example of intersection_updates of set.
a = {53,67,23,87,34}
b = {23.1,12,42,87,34}
a.intersection_update(b)
print(a,b)

# this is the example of symmetric_difference of set.
a = {23,53,52,13}
b = {23,14,55,34}
print(a.symmetric_difference(b))

# this is the example of difference() set.
a = {12,"harry","nora","34",(23,45,"abhishek")}
b = { "new","go"}
print(a.difference(b))

# this is the example of isdisjoint():
a = {"delhi","kanpur","jaipur"}
b = ("kolkata","nanital","shivpura")
print(a.isdisjoint(b))
a1 = {"delhi","kanpur","jaipur"}
b1 = ("delhi","nanital","shivpura")
print(a1.isdisjoint(b1))

# this is the example of issuperset().
a = {"delhi","kanpur","jaipur"}
b = {"delhi","kanpur"}
print(a.issuperset(b))

# this is the example of issubset().
a = {"delhi","kanpur","jaipur"}
b = {"delhi","kanpur"}
print(b.issubset(a))

# this is the example of add().
a = {"add","subtract","multiply","divide"}
a.add("brackets")
print(a)

# this is the example of remove()/discard().
a = {"delhi","punjab","kolkata","tamil nadu","chennai","aligarh"}
a.remove("aligarh")   # Note: they will show error if the item is not present in the set when we are removing the item. 
print(a)
a.discard("punjab")   # Note: it will not show error if the item is not present in the set when we are removing the item.
print(a)

# this is the example of pop().
a = {"delhi","punjab","kolkata","tamil nadu","chennai","aligarh"}
item = a.pop()
print(a)
print(item)

# this is the example of del.
a = {"delhi","punjab","kolkata","chennai","pune"}
# print(a)
del a

# this is an example of clear().
a = a = {"delhi","punjab","kolkata","chennai","pune"}
a.clear()      # it gives an empty set.
print(a)
