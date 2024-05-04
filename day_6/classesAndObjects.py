class Person:
    name: "Sharabh"
    occupation: "Developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")




a = Person()
a.name = "Rachael"
a.occupation = "FBI agent"
a.info()

b = Person()
b.name = "Tatiana"
b.occupation = "Wedding Organiser"
b.info()

# using constructor in class

class Business:
    # dunder method
    def __init__(self, ind="forex", founded="2009"):
        self.industry = ind
        self.founded = founded

    def show(self):
        print(f"This company was founded on {self.founded} and in the industry of {self.industry}")


x = Business("entertainment", 2010)
y = Business()
x.show()
y.show()