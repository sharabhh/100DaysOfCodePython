'''
Write a program to print the following star pattern.
* * *
* * for n = 3
* * *
'''
rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    if(i == 0 or i== rows):
       print("*" * rows)
    else:
       print("*", end="")
       print(" " * (rows - 2), end="")
       print("*", end="")
    print("")