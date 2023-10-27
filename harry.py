def show():
      user = ["abhishek","vivek","shivam","avinash","ashish","rupak","anurag"]
      for index,value in enumerate(user,start=1):
            if __name__ == "__main__":
              print(index,value)

show()

def welcome():
    print("hello everyone this side is abhishek and i am going to run this code.")

print(__name__)
if __name__ == "__main__":    # this is used to avoid the duplication of code when we import the scratch file from one place to another 
  welcome()
