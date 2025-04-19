# Write a program to print multiplication table of a given number using for loop. using while loop
num = int(input("Enter a number for it's multiplication table: "))

i = 1
while (i<11):
    print(f"{num} x {i} = {num * i}")
    i += 1