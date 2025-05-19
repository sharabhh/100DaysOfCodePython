# Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

class TwoDVector:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def showTwo(self):
        print(f"{self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i,j,k):
        super().__init__(i, j)
        self.k = k

    def showAll(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

x = TwoDVector(2,4)
x.showTwo()
y = ThreeDVector(2,3,4)
y.showAll()