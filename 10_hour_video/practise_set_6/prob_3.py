# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

message = str(input("Enter the message: "))

list1 = []
list1.append(message)

if((list1.count("Make a lot of money") > 0) or (list1.count("buy now") > 0) or (list1.count("subscribe this") > 0) or (list1.count("click this") > 0)):
    print("Spam detected")
else:
    print("No spam detected")