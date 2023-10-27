# in this session we will learn about the if-elif-else condition.

# sometime the programmer needs to check the evaluation of certain expression.whether the expression evaluation is True or False.if the expression evaluation to False,then the program execution follows a different path than it would have if the expression had evaluated to True.
# Conditional operators are of many types for ex:
# 1)  > --- greater than conditional operator
# 2)  < --- lesser than conditional operator
# 3)  >= --- greater than equal to conditional operator
# 4)  <= --- lesser than equal to conditional operator
# 5)  == --- equal to conditional operator
# 6)  != --- not equal to conditional operator
# 7)  Nested - if,if-else,elif ---> we can use if,if-else,elif statements inside other if statement as well.

a = int(input("enter your age: "))
if a >18:
    print ("you are eligible to vote.")   # Note: here space is called as 'indentation'.it indicates that we are starting a block.

b = int(input("enter your favourite number: "))
c = int(input("enter your second favourite number: "))
if b==c:
    d = int(input("enter your third number: "))
    if d>c:
        print("d is greater than a & b")
elif a>b:
    print("this is world famous tony stark.")

elif a<b:
    e = int(input("enter your lucky number: "))
    if a==e :
        print("this is captain america and black widow.")
else:
    print("thanks! nice to meet you.")    # this is the example of nested if-else condition.
    