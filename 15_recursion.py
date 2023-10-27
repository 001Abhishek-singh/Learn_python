# in this session we will learn about the recursion.

# Recursion ---> it is the process of defining something in terms of itself.
# Recursive function ---> it is even possible for the function to call itself.these type of construct are termed as recursive functions.we know that a function can call other function.

def factorial(n):
    if (n==0 or n==1) :
      return 1
    else:
       return  n * factorial(n-1)
print(factorial(7))


#(example 1) we can access the else with for & while loop.
user = int(input("enter your number: "))
for i in range(user):
    print("Jai shree ram !")
else:
    print("jai maa chamunda ! ")

#(example 2) this is a second example of loop with else.. 
user = int(input("enter your number: "))
for i in range(user):
    print("JAI JAI JAI BAJRANGBALI !")
    if user == 109:                                   
        break                                       #(as the user put 109 then program will break and it will display the line which is mention above the break statement.)
else:
    print("mere prabhu ram aaye hai.")

    