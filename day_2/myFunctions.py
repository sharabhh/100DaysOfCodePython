import math

def pythagoras(base,perpendicular):
        hypotenuse = math.sqrt(base*base + perpendicular*perpendicular)
        return hypotenuse
    
    
def noUse():
    # pass tells the interpreter to ignore the function for now as I'll define it later
    pass

print(pythagoras(4,3))