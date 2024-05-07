# super keyword helps access the function of parent class from the child class.

class Parent:
    def parentMethod(self, location):
        self.location = location
        print("I am the parent.")

class Child(Parent):
    def childMethod(self, location):
        print("I am a child method.")
        # writing super specifies that when we call the function it has to search in the parent class. and if we don't write super() It will try to find a similiar name function in the child class.
        super().parentMethod(location)

c = Child()
c.childMethod("jhansi")
print(c.location)