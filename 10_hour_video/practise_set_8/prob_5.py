# Write a python function which converts inches to cms.

inches = int(input("Enter the length in inches: "))
def inch_to_cm(inches):
    return inches * 2.54
print(f"The length in cm is: {inch_to_cm(inches)}")