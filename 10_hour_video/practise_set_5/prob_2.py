# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
num6 = int(input("Enter sixth number: "))
num7 = int(input("Enter seventh number: "))
num8 = int(input("Enter eighth number: "))

num_set = set()
num_set.add(num1)
num_set.add(num2)
num_set.add(num3)
num_set.add(num4)
num_set.add(num5)
num_set.add(num6)
num_set.add(num7)
num_set.add(num8)
print("The unique numbers are: ", num_set)