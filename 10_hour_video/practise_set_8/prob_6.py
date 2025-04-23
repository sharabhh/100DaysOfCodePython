# Write a python function to remove a given word from a list ad strip it at the same
# time.

item1 = str(input("Enter the first item: "))
item2 = str(input("Enter the second item: "))
item3 = str(input("Enter the third item: "))
word = str(input("Enter the word to be stripped: "))
list_of_items = [item1, item2, item3]

def strip_items(items, word):
    l = []
    for item in list_of_items:
        if not (item == word):
            l.append(item.strip()) 
    return l

print(f"new list is {strip_items(list_of_items, word)}")
    