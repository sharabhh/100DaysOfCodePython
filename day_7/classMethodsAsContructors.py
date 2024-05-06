class Employee:
    def __init__(self, name):
        self.name = name

    @classmethod
    def addName(cls, data):
        return cls(data.split("-")[0] + " "+ data.split("-")[1])

e1 = Employee("Sharabh")
print(e1.name)
str = "Sharabh-Mishra"
e1 = Employee.addName(str)
print(e1.name)