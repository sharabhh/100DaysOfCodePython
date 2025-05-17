# Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {pow(self.num, 2)}")
    
    def cube(self):
        print(f"The cube of {self.num} is {pow(self.num, 3)}")
    
    def sqrt(self):
        print(f"The squareroot of {self.num} is {pow(self.num, 1/2)}")

    
obj1 = Calculator(4)
obj1.square()
obj1.cube()
obj1.sqrt()