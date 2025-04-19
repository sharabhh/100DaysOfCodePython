# Write a program to find whether a given number is prime or not.
num = int(input("Enter a number to detect if it is prime: "))

count = 0
for i in range(1, num+1):
    if(num % i == 0):
        count += 1

if(count >2):
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")