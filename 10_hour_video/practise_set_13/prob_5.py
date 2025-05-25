# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

l = [1,5,99,2,8,56,10]

def myfunc(a,b):
    if a>b:
        return a
    return b
newValue = reduce(myfunc, l)
print(newValue)