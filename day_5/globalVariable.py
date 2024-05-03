# We can use global keyword to change values of global variables inside a function

x = 5

def changleGlobal():
    global x
    x = 10

print(x)
changleGlobal()
print(x)