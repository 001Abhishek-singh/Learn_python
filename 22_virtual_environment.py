# (16/02/2023) Today we are going to learn a very important lesson in python that is how to create a 'Virtual environment' for version control in python programming session.

'''Virtual environment ---> it is a tool used to isolate specific python environment on a single machine,allowing us to work on multiple projects with different dependencies and packages without conflicts.this can be especially useful when working on projects
that have conflicting packages versions or packages that are not compatible with each other.Once the virtual environment is activated,any packages that us install using pip will be installed in the virtual environment,rather than in the global python environment.this allows us to have a separate set of 
packages for each project,without affecting the packages installed in the global environment.'''
# How to create a virtual environment.
''' Python -m venv myenv  ---> this is a basic statement which is used to create a virtual environment.'''
# Activate the virtual environment.(Linux / mac Os)
''' Source myenv/bin/activate ---> this is used to activate the virtual environment in the linux and in mac os.'''
# Activate the virtual environment.(Windows)
''' myenv\Scripts\activate.bat ---> this is used to activate the virtual environment in windows.
    myenv\Scripts\activate.ps1 (if we are working in a powershell than use this command to activate the virtual environment in it.)'''
# Deactivate the virtual environment.(for all)
''' Deactivate ---> this statement is used to deactivate the virtual environment.'''


# The "requirements.txt" file
''' requirements.txt ---> in addition to creating and activating a virtual environment.it can be useful to create a requirements.txt file that list the packages and their version that our project depends on.This file can be used to easily install all the required packages in a new environment.
To create a requirements.txt file,we can use the pip freeze command,which outputs a list of installed packages and their version.'''
# To get a list of installed packages and their version in a file,we use the below command.
''' pip freeze > requirements.txt ---> this command will help to get the list of installed packages in that virtual environment.'''
# For installing the installed packages and their version from one venv to another venv,we simply use the below command.
''' pip install -r requiements.txt ---> through this packages will install in the venv.'''
# if we want to check the installed packages in the given virtual environment than we will use the following command.
''' pip freeze ---> this will simply display the installed packages in the given virtual environment.'''

'''using the venv and requirements.txt file this can help us to manage the dependencies for our python projects and ensure that our projects are portable and can be easily set up on a new machine.'''
