from functools import reduce

l = [1, 2, 3, 4, 5]
m = [4, 6, 8, 9, 0]


def double(x):
    return x * 2

def filtration(x):
    return x>=2

# since map function returns a map object we surrond it woth list to make a list
result = list(map(double, l))
print("Map result is:",result)

filtrationResult = list(filter(filtration, l))
print("Filter result is:",filtrationResult)
# we can also add mulyiple parameters and lambda function too

newResult = list(map(lambda x,y: x*y, l,m))
print("New list is:", newResult)

# REDUCE FUNCTION

reduceResult = reduce(lambda x,y: x+y, l)
print("Reduce result is: ", reduceResult)