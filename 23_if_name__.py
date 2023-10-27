# Today we are going to learn about the if__name__ == "__main__" method in python.

# if "__name__ == "__main__"" in python.
'''The if __name__ == "__main__" idiom is a common pattern used in python scripts to determine whether the script is being run directly or being imported as a module into another script.
In python,the __name__ variable is a built-in-variable that is automatically set to the name of the current module.when a python script is run directly,the __name__ variable is set to the string 
__main__ when the script is imported as a module into another script.the __name__ variable is set to the name of the module.'''

# let's understand it by an example.
def welcome():
    print("hello everyone this side is abhishek and i am going to run this code.")

print(__name__)
if __name__ == "__main__":    # this is used to avoid the duplication of code when we import the scratch file from one place to another 
  welcome()
'''In this example,the main function contains the code that should be run when the script is run directly.the if statement at the bottom checks whether the __name__ variable is equal to __main__.if it is,the main function is called.'''

# Why is it useful ? 
'''This idiom is useful because it allows us to reuse code from a script by importing it as a module into another script,without running the code in the original script.
if we run any script directly,it will give output.however,if we import it as a module into another script and call the main function from the imported module,it will not provide any output.'''

from harry import welcome
welcome()

