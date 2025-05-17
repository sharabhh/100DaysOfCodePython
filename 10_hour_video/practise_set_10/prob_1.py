class Programmers:
    company = "Microsoft"
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def getInfo(self):
        print(f"{self.name} is a {self.role} at {self.company}")

obj1 = Programmers("Sharabh", "Cheif Programmer")
obj1.getInfo()