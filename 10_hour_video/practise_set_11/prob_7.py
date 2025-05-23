# Override the __len__() method on vector of problem 5 to display the dimension of the vector

class Vector:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    
l = Vector([1,2,3, 4])
print(l.__len__())