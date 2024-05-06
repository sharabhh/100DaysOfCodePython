class Employee:
    def __init__(self, eId, name):
        self.empId = eId
        self.name = name

    def show(self):
        print(f"The name of Employee: {self.empId} is {self.name}")

# inheriting Employee class
class Programmer(Employee):
    def info(self):
        print("Programmer uses Python")


# a = Employee(400, "Adele")
# a.show()
a = Programmer(400, "Adele")
a.info()
        