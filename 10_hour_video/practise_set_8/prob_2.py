# Write a python program using function to convert Celsius to Fahrenheit
degree = int(input("Enter the temperature in Celsius: "))

def celsius_to_fahrenheit(degree):
    return (degree * 9/5) + 32

print(f"The temperature in fahrenheit is {celsius_to_fahrenheit(degree)}")