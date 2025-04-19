# Write a program to find the sum of first n natural numbers using while loop.
num = int(input("Enter a number: "))

if(num <= 0):
    print("Please enter a natural number")
sum = 0
for i in range(1, num+1):
    sum+=i

print(f"The sum of all numbers from 1 to {num} is {sum}")