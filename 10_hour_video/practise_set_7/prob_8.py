'''
Write a program to print the following star pattern:
*
**
*** for n = 3
'''

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print("*" * i + "\n")

