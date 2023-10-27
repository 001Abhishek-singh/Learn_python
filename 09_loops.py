# today we will learn about the loop concept.

# Loop ---> sometime a programmer needs to execute a group of statements for a certain no. of times.this can be performed by loops.based on this loop concept it is futher classified into three group such as:
# 1) for loop ---> for loop can iterate over a sequence of iterable objects in python.Iterating over a sequence is nothing but iterating over string,set,tuple,dictionary,list,etc.they have various methods 
# 1a) range method
# 2) while loop 
# Part of a loop ---> break and continue 
# a) break ---> it will enable a program to stop over a part of the code("Note: leave the loop").a break statement terminates the very loop it lies within. it will break the iteration in a loop.
# b) continue ---> it will skip the rest of the loop statements and causes the next iteration to occur("Note: leave the iteration").
'Note: iterable object ---> '

user = input("enter your name: ")
for i in user:                  # here i is variable which is used to iterate every character of the string.
    print(i) 

a = int(input("enter your favourite number: "))
for i in range(a,1,-2):        # here "a is start argument","1 is end argument","-2 is step(omit the value) parameter"
    print(i)

user2 = int(input("enter the number: "))
user3 = input("enter the name: ")
for i in range(0,user2):
    print(i)

colors = ['red','pink','yellow','orange','purple']
for value in colors:
    print(value)
    if value == 'red':
        print("thid is my favourite color.")
        for i in value:
            print(i) 

# now we will make a syntax for the while loop.
i = 0
while (i<5):
    print(i)
    i = i+1

# now i am making a program to invite the relative in marraige.
i = 0
user = input("enter the name of invitee: ")
print(user,"has been invited.")
while(i<12):
    a = input("do you want to invite more person: ")
    if a =="yes" or a =="YES" or a == "Yes":
        user = input("enter the name of invitee: ")
        print(user,"has been invited.")
        i =i+1
    else:
        print(user)
else:
    print("Thank you so much.") 

# break and continue         
i = 0
while(i<12):
    i=i+1
    if i == 1:
        continue        # it will skip the iteration in loop.
    print("5x",i,"=",5*i)
    if i == 10:
        break           # it will skip the loop.
print("Thank you so much.")
