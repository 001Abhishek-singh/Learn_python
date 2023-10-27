# today we will learn about the match case statement.

# Match ---> this is a new edition case statement in python which is come after the python 3.10.version 
'''this is just like a switch statement, switch statements are functionally similar to if-else statements,but they require less code when defining the cases.this is more 
powerful and allows for more complicated pattern matching.
    Match case consist of three main entities;
    1) The match keyword
    2) One or more case clauses
    3) Expression for each case'''

user = int(input("Enter the value of user: "))
match user:
    case 0:
        print('this is tony stark')
    case 2:
        print('this is captain america.')
    case 3:
        print('this is black widow')
    case _:
        print("this is black panther.")
        

print("Who is not ever the prime minister of INDIA ? \n kapil sharma\n Narendra modi \n Indra gandhi \n Manmohan singh")  

user2 = input("Choose the correct answer of the following question: ")

match user2:
    case 'kapil sharma':
        print("Congrats! you are correct.")
    case 'Narendra modi':
        print("Oops! you are wrong.")
    case 'indra gandhi':
        print("Oops this is rediculous.")
    case 'Manmohan singh':
        print("Pathetic you are wrong")
         
