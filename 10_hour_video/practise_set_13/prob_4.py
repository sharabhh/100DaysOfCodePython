# Write a program to filter a list of numbers which are divisible by 5.
l = [1,2,3,4,5,6,7,8,25,9,10, 15]

def myfunc(x):
    if x% 5 == 0:
        return True
    return False

newL = filter(myfunc, l)
for i in newL:
    print(i)