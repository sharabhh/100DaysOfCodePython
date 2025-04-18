# Check that a tuple type cannot be changed in python.
tup = (1,2,3)

tup[2] = 4 # This will raise a TypeError because tuples are immutable
print(tup)
