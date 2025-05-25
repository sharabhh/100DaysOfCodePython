# Store the multiplication tables generated in problem 3 in a file named Tables.txt.


number = int(input("Enter the number to calculate the table for: "))
table = [number*i for i in range(1,11)]
print(table)
# str_of_Table = "\n".join(table)

with open("Tables.txt", "a") as f:
    f.write(str(table) + "\n")