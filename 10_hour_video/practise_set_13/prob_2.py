# Write a program to input name, marks and phone number of a student and format it using the format function like below:

name = str(input("Enter the name: "))
marks = int(input("Enter the marks: "))
phno = str(input("Enter the phone number: "))

formattedString = "The name of the student is {0}, his marks are {1} and phone number is {2}".format(name, marks, phno)
print(formattedString)