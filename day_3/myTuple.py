# tuples are immutable you need to change them to lists to make changes in them

x = (1,3,6,4,7)
y = list(x)
y.append(24)
print(y)
# x= tuple(y)
print(x)