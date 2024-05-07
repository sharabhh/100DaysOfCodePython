# dir()  In Python, the dir() function is a built-in function used to list the attributes (methods, properties, and other members) of an object.

x = [1,2,3]
print(dir(x))


# __dict__ List all attributes of a class as a dictionary (object)

class Restaurant:
    def __init__(self):
        self.name= "Sharabh"
        self.designation = "coder"

r = Restaurant()
print(r.__dict__)


# help In Python, the help() function is a built-in function that provides information about modules, classes, functions, and modules.

print(help(r))