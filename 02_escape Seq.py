# in this session we will learn about comments,escape sequences and print statement.

# ---> this is a normal comment character   ----  this is a single line comment.
''' this is a multiple line comment character'''   # ''' ''' ----> this indicate the triple single quote,use to comment out multiple lines.  
""" this is also a multiple line comment character """  # """ """ ----> this indicate the triple double quote,use to comment out multiple lines.
# ---> \n this is a new line escape sequence character.   ---  used to go on new line without disturbing the statement.
# ---> \" this is a back slash double quote escape sequence character. --- used to put the word or statement in double quoted comma.
# ---> \' this is a back slash single quote escape sequence character. --- used to put the word or statement in single quoted comma
# ---> "sep" this is a print parameter used to separate the character
# ---> "end" this is a print parameter used to end with some of the character.


user = "hello world i am tony stark and you know this world is for \'you and for your\' entire family"
print(user)

user1 = " hello user this side is abhishek and my roll no. is \"200202010049\" and after putting this roll no. you will get my data without any disturbances."
print(user1)

user2 = "twinkle twinkle little star \n how you wonder what you are\n up the sky what you are \n like a wonder up the sky."
print(user2)

user3 = " hello world this side is tony stark and i am the inventor of the jarvis"
print(user3,4,5,66,sep="-")

user4 = "this side is tony stark and i am the inventor of ultron and vision"
print(user4,44,7895,sep="-",end="\nTHANK YOU SO MUCH")