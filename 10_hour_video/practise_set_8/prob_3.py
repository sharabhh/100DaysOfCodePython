# Write a recursive function to calculate the sum of first n natural numbers.
n = int(input("Enter a number: "))

def sum(x):
    if x == 1:
        return 1
    return x + sum(x-1)

print(f"The sum of first {n} natural numbers is: {sum(n)}")