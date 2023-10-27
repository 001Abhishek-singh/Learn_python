# today we will learn about the string and there uses.

user = input("enter your name: ")
print(user)    # here data written in double quoted common's is known as string.
print(user[0])  # here big bracket indicate the string slicing where we can find out the particular value at the given index number.
# big bracket with the number generally use for finding the index value.
for word in user:
    print(word)

# string slicing ---> we can find out the index value of the string and we can take the value from the string by using the string slicing with the help of index value.

user1 = "abhishek"
print(user1[0:3]) # here python start from 0 but it does not include 3 because it will only consider 0,1 & 2.

'''user2 = "vivek singh"
print(len(user2))  # here len function used to predict the length of the given string.'''

user3 = "kunal singh"
print(user3[0:-3]) # here it will show the value of string from 0 to -3(2). basically here,they perform string slicing from 0 to 'len(variable)-3'.

# STRING METHODS:
'Note: strings are immutable','we can overwrite a variable in a python.'
# 1) upper method ---> to convert the string into upper case.
# 2) lower method ---> to convert the string into lower case.
# 3) rstrip method ---> it will remove the trailing character."it will not remove the leading character for ex: !!!!vivek -- output -- !!!!vivek.","it will remove the trailing character for ex: vivek!!!! -- output -- vivek."
# 4) replace method ---> it will replace the string."all string occurance will replace."
# 5) split method ---> it will convert the string into list."space must be present between two consecutive string then only they will make a list of items."
# 6) capitalize method ---> used to convert the first alphabet of a string into capital letter.
# 7) center method ---> this will shift the string to the center from a given distance.
# 8) count method ---> this will reflect how many times a character occur in a string.
# 9) endswith method ---> this will reflect that a particular character will ends with or not in a particular string."it will give a boolean datatype in answer."
# 10) find method ---> it will find the first occurances of the given value and return the index no. where it is present.if given value is absent from the string then they will return -1 as output.
# 11) index method ---> it will find the first occurances of the given value and return the index no. where it is present.if the character is not present in the string then exception value(error) will be shown in the output.
# 12) isalnum method ---> it will return true if the entire string only contain alpa-numeric A-Z,a-z,0-9.if they contain any other character or puntucation then it return false.
# 13) isalpha method ---> it will return true if the entire string only contain A-Z,a-z.if any other character,punctuation and number are present then it return false.
# 14) islower method ---> it will return true if all the characters in the string are lower case,otherwise it return as false.
# 15) isprintable method ---> it will return true if all the value within the given string are printable.if not,then return false.
# 16) isspace method ---> it will return true only and only if the string contain white spaces,else return false.
# 17) istitle method ---> it will return true only when if the first letter of each word of the string is capitalize,else it return false.
# 18) isupper method ---> it will return true if all the character in the string are upper case,otherwise it return false.
# 19) startswith method ---> this will reflect that a particular character will start with or not in a particular string."it will give a boolean datatype in output."
# 20) swapcase method ---> it convert the character casing of the string,upper case are converted into lower case and lower case converted into upper case.
# 21) title method ---> it capitalize each letter of the word within the string.


a = "vivek!!!"
print(a)
print(a.rstrip("!"))

b = "vivek@"
print(b.replace("vivek","anurag"))

c = " harry, vivek, abhishek, shubham, kajal"
print(c.split(" "))

d = "introduction to world"
print(d.capitalize())

e = "welcome to electrical mania."
print(e.center(45))

f = " abhishek is goat and gave a awesome treat to everyone."
print(f.count("a"))

g = "hello world this side is tony stark the inventor of ultron and vision."
print(g.endswith("vision"))
print(g.endswith("the",4,35))  # here we checked that 'the' exist between index no.4 to 35 or not by using the endswith method.

h = "hello world this side is abhishek."
print(h.find("w"))
print(h.find("kumar"))

i = "hello world this side is abhishek."
print(i.index("world"))
#print(i.index("ishhsh"))

j = " HelloWorldThisIsKumarSanu1"
print(j.isalnum())

k = "GoodWorld" 
print(k.isalpha())

m = "jai shree ram"
print(m.islower())

n = "jai shree ram\n"
n2 = "jai shree ram"
print(n.isprintable())
print(n2.isprintable())

o = "   " # space will be given by using the Spacebar or tabbar.
print(o.isspace())

p = "Hello World"
print(p.istitle())

q = "helloworld"
print(q.swapcase())

r = " your blood is blood and my blood is water how is it possible."
print(r.title())



