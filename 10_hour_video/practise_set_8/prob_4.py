'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*

'''
rows = int(input("Enter the number of rows: "))

def print_pattern(x):
    y = x
    if y == 1:
        return '*'
    return '* ' * x + '\n' + print_pattern(x-1)


print(print_pattern(rows))