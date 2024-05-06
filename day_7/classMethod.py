class Employee:
    company = "TESLA"
    # def __init__(self):
        # self.company = "TESLA"

    # class methods are used to change predefined
    @classmethod
    def changeCompany(cls, compName):
        cls.company = compName


e1 = Employee()
print(e1.company)
e1.changeCompany("APPLE")
print(e1.company)
print(e1.company)