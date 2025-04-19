# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number: "))

if(num < 0):
    print("Please enter a non-negative number")
if(num == 0):
    print("The factorial of 0 is 1")
result = 1
for i in range(1, num+1):
    result *= i
    # print(f"{num} x {i} = {num * i}")

print(f"The factorial of {num} is {result}")