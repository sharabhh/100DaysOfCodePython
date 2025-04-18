# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

name = str(input("Enter your name: ")).capitalize()
date = str(input("Enter the date: "))
letter = f"Dear {name} \nYou are selected!\n{date}"
print(letter)