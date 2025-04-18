# Write a program to detect double space in a string.

l = "hi  there"
b = l.find("  ")
if b == -1:
    print("No double space found")
else:
    print("Double space found at index:", b)
# print(b) # This will print the index of the first occurrence of double space in the string