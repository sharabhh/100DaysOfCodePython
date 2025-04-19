# Write a program which finds out whether a given name is present in a list or not.

list1 = ["randy", "anne", "john", "jane", "billie"]
username = str(input("Enter the username: "))
if(list1.count(username) > 0):
    print("Username already exists")
else:
    print("Username is available")
    list1.append(username)
    print("Updated list of usernames: ", list1)