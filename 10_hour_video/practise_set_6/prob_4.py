# Write a program to find whether a given username contains less than 10
# characters or not.

string = str(input("Enter the username: "))
if(len(string) < 10):
    print("The username contains less than 10 characters")
else:
    print("The username contains more than 10 characters")