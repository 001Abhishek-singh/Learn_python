# In this session we are going to learn about the dictionary.

'''Dictionary ---> it is a ordered collection of data items.they store multiple items in a single variable.dictionary items are "key-value" pairs that are separated by commas and enclosed within curly brackets.'''
# Dictionary Method:
# 1) update() method ---> this will update the value of the key provided to it.if the item already exists in the dictionary,else it creates a new key-value pair.
# 2) clear() method ---> this method removes all the items from the list.
# 3) pop() method ---> this method removes the key - value pair whose key is passed as a parameter.
# 4) popitem() method ---> this method removes the last key-value pair from the dictionary.
# 5) del ---> this is keyword to remove a dictionary item.

# this is the example of dictionary.
a = {"harry":"coder"
    ,"abhishek":"student"
    ,"vivek":"IAS Officer"
    ,"shivam":"IAS Officer"
    ,"anurag":"listner"}
print(a["anurag"])   # here we accessing single key-value pair.
print(a["harry"])
print(a["shivam"])
print(a["abhishek"])

# this is another example of dictionary.
a = {121 : "abhishek",
         141 : "vivek",               # here we accessing single key-value pair.
         131 : "shivam",
         161 : "avinash",
         191 : "ashish"}
print(a[121])
print(a[191])

# this is the example of dictionary where we access single values:
user = {"name":"abhishek","yes":'FOR WHAt',"good":"better"}
print(user)
print(type(user))         # variable_name[key name]/variable_name.get(key name) ---> to obtain the value of key in dictionary.
print(user["good"])       # Note: if we write the wrong key name which is not present in the dic. then this syntax will show error in output.
print(user.get("good"))   # Note: if we write the wrong key name which is not present in the dic. then this syntax will show "none" as a output.

# this is the example of dictionary where we access the multiple value:
user = {"name":"abhishek","surname":"singh","title":"kumar","age":21}
print(user)
print(user.keys())    # this will give all the keys of the dictionary.
print(user.values())  # this will give all the values of the dictionary.

# this is the another example of dictionary where we access the multiple value: 
user = {141 : "vivek",              
         131 : "shivam",
         161 : "avinash",
         191 : "ashish"}
for i in user.keys():        # this will use to access the multiple keys by using the loop condition.
    print(i)
for i in user.values():      # this will use to access the multiple values by using the loop condition.
    print(i)

# this is an example of key-value pairs:
user = {"name":"abhishek","surname":"singh","title":"kumar","age":21}
print(user.items())

# example of update method.
user2 = {344:23,231:54,421:92,871:99}
user1 = {234:67,562:85,811:87}
user2.update(user1)
print(user2)

# example of clear method.
user2 = {344:23,231:54,421:92,871:99}
user2.clear()  # it will give empty dictionary.
print(user2)

# example of pop method.
user2 = {344:23,231:54,421:92,871:99}
user2.pop(344)
print(user2)

# example of popitem().
user2 =  {344:23,231:54,421:92,871:99}
user2.popitem()             # it will remove the last key-value pair from the dictionary.
print(user2)

# example of del.
user2= {344:23,231:54,421:92,871:99}
del user2
print(user2)
