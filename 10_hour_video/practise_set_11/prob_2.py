# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    a = "animals"

    def __init__(self):
        print(f"This is {self.a} class __init__")

class Pets(Animals):
    b = "Pets"
    def __init__(self):
        print(f"This is {self.b} class __init__ which is a inherited class of {self.a}")
    

class Dog(Pets):
    c = "Dog"
    def __init__(self):
        print(f"This is the {self.c} class which is the inherited class of {self.b} class __init__ which is a inherited class of {self.a}")
    
    def bark(cls):
        print("woof woof")

x = Dog()
x.bark()