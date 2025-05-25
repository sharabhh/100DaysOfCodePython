# A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
# l = [7, 14, 21, 28, 35, 42, 49, 54, 63, 10]

table = [str(7*i) for i in range(1,11)]
newStr = "\n".join(table)
print(newStr)
