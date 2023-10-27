# today we are going to learn about the tuple.

# Tuple ---> tuple are ordered collection of data items.they store multiple items in a single variable.tuple items are separated by comma and enclosed within round brackets().they are immutable(cannot changeable) once created.
# Tuple method:
# 1) Manipulating the tuples:  tuples are immutable hence if we want to add,remove or change tuple items.then first you ust convert the tuple to a list than perform operation on that list and convert it back to tuple.
# 2) we can directly concatenate two tuples without converting them to list.
# 3) count()method ---> this will give the number of times the given element appears in the tuple.
# 4) index() method ---> this method returns the first occurance of the given element from the tuple.
# 5) len() method ---> this method will use to find out the length of the tuple.

user = (14,23,54,"string","data",True,23.56,67)
print(user)
print(type(user))

user1 = (1)  # here this syntax shows that it is act as integer
print(type(user1))

user2 = (1,)  # now here with the help of comma we can change the integer into tuple.
print(type(user2))

print(user[1])     # this indicate the indexing of the tuple.
print(user[-2])     # this indicate the negative indexing of the tuple.

print(user[:])      # this is slicing of the tuple but noted that tuple cannot be change after the slicing this will give "new tuple".
print(user[:-2])

if "nora" in user:      # to check the item present in the tuple or not.
    print("Good to go.....")
else:
    print("Oops! this item is not in your tuple.")

countries = ("india","america","pakistan","butan","china")
# now we convert the tuple into list 
coun = list(countries)
# now we add russia in the list.
coun.append("russia")
# now we will remove(pop) the item from the list.
coun.pop(2)
# now we will replace the item from the list by using the index slicing method.
coun[-2] = "france"
# now again we convert the list into tuple. 
countries= tuple(coun)
# now we will print the tuple
print(countries)

# here we directly concatinate the two tuples.
countries_1 = ("india","japan","russia",'germany')
countries_2 = ("america","spain","uk","dubai")
countries_3 = countries_1 +countries_2
print(countries_3)

# here we check the count and index method of the tuple.
countries_1 = ("india","japan","russia",'germany')
print(countries_1.count("japan"))       # it will indicate the number of items present in the tuple.

countries_1 = ("india","japan","russia",'germany')
print(countries_1.index("germany"))    # it will give the index number of the tuple.

# we can check the length of the tuple.
countries_1 = ("india","japan","russia",'germany')
print(len(countries_1))  