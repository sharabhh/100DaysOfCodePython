# Write __str__() method to print the vector as follows:

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j+ {self.z}k"

v1 = Vector(1, 2, 3)

print(v1.__str__())