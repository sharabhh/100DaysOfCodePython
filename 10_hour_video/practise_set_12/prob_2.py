# Write a program to print third, fifth and seventh element from a list using enumerate function.

list = ["sharabh", "mishra","tasmiah", "ahmed", "harshit", "bagwar", "jai", "tomar", "dushyant", "verma"]

for i, name in enumerate(list):
    if (i == 3 or i == 5 or i==7):
        print(f"The value of index: {i} is = {name}")